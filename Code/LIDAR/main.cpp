#include <cmath>
#include <ctime>
#include <signal.h>
#include <stdio.h>
#include <unistd.h>

#include "sl_lidar.h"
#include "sl_lidar_driver.h"

/* Début boilerplate */
#ifndef _countof
#define _countof(_Array) (int)(sizeof(_Array) / sizeof(_Array[0]))
#endif

static inline void delay(sl_word_size_t ms)
{
    while (ms >= 1000)
    {
        usleep(1000 * 1000);
        ms -= 1000;
    };
    if (ms != 0)
        usleep(ms * 1000);
}

using namespace sl;
/* Fin boilerplate */

enum LIDAR_ERR
{
    LIDAR_NO_MEM = -1,
    LIDAR_NO_CHANNEL = -2,
    LIDAR_NO_CONN = -3,
    LIDAR_UNHEALTHY = -4,
};

const unsigned int baudrate = 460800;
const char serial_device[13] = "/dev/ttyUSB0";
const FILE *f_out = stdout;
bool program_should_quit = false;

bool checkSLAMTECLIDARHealth(ILidarDriver *drv);
void end_program(int sig);

/*
On veut regarder l'arène :

    +-----------------------------------+
    |                                   |
    |                                   | 2
  1 |                                   |
    |                                   |
    |                                   | 3
    |                                   |
    +-----------------------------------+

On veut ensuite trouver l'ordre des balises pour calculer notre position.
En effet, le problème est qu'on ne peut pas donner les balises dans un
ordre quelconque, sinon on prend le risque d'avoir une position biscornue.

Enfin, on calcule leur position théorique relative à notre robot, en distance
et angle, puis on compare avec ce que l'on a par le LIDAR.
*/

extern int pos_x, pos_y;

void compute_theoritical_pos(float &cur_x, float &cur_y, float delta_x, float delta_y);
void next_beacon_pos(float &dist, float &angle, float next_x, float next_y);

int main()
{
    Result<ILidarDriver *> _driver = createLidarDriver();
    if ((bool)_driver == false || *_driver == NULL)
    {
        fprintf(stderr, "[LIDAR::driver] Manque de mémoire pour créer un driver ! Abandon...\n");
        exit(LIDAR_NO_MEM);
    }
    ILidarDriver *driver = *_driver;

    sl_lidar_response_device_info_t devinfo = {0};

    Result<IChannel *> _ch = createSerialPortChannel(serial_device, baudrate);
    if ((bool)_ch == false || *_ch == NULL)
    {
        fprintf(stderr, "[LIDAR::driver] Manque de mémoire pour créer un channel vers le LIDAR ! Abandon...\n");
        delete driver;
        exit(LIDAR_NO_CHANNEL);
    }
    IChannel *channel = *_ch;

    if (SL_IS_FAIL(driver->connect(channel)) || SL_IS_FAIL(driver->getDeviceInfo(devinfo)))
    {
        fprintf(stderr, "[LIDAR::driver] Echec lors de la connexion au LIDAR ! Abandon...\n");
        delete driver;
        delete channel;
        exit(LIDAR_NO_CONN);
    }

    if (!checkSLAMTECLIDARHealth(driver))
    {
        // delete channel;
        delete driver;
        exit(LIDAR_UNHEALTHY);
    }

    signal(SIGINT, end_program);

    driver->setMotorSpeed();
    driver->startScan(false, true);

    while (true)
    {
        size_t count = 8192;
        sl_lidar_response_measurement_node_hq_t nodes[count];
        sl_u64 timestamp;

        sl_result op_result = driver->grabScanDataHqWithTimeStamp(nodes, count, timestamp);

        if (SL_IS_OK(op_result))
        {
            driver->ascendScanData(nodes, count);
            for (int pos = 0; pos < (int)count; ++pos)
            {
                printf("%s theta: %03.2f Dist: %08.2f Q: %d \n",
                       (nodes[pos].flag & SL_LIDAR_RESP_HQ_FLAG_SYNCBIT) ? "S " : "  ",
                       (nodes[pos].angle_z_q14 * 90.f) / 16384.f, nodes[pos].dist_mm_q2 / 4.0f,
                       nodes[pos].quality >> SL_LIDAR_RESP_MEASUREMENT_QUALITY_SHIFT);
            }
        }

        if (program_should_quit)
        {
            break;
        }
    }

    driver->stop();
    delay(200);
    driver->setMotorSpeed(0);

    delete driver;
    delete channel;

    return 0;
}

/* Pris du programme d'exemple `app/ultra_simple/main.cpp` */
bool checkSLAMTECLIDARHealth(ILidarDriver *drv)
{
    sl_result op_result;
    sl_lidar_response_device_health_t healthinfo;

    op_result = drv->getHealth(healthinfo);
    if (SL_IS_OK(op_result))
    { // the macro IS_OK is the preperred way to judge whether the operation is succeed.
        printf("SLAMTEC Lidar health status : %s\n", healthinfo.status == 0   ? "OK"
                                                     : healthinfo.status == 1 ? "WARNING"
                                                                              : "ERROR");
        if (healthinfo.status == SL_LIDAR_STATUS_ERROR)
        {
            fprintf(stderr, "Error, slamtec lidar internal error detected. Please reboot the device to retry.\n");
            // enable the following code if you want slamtec lidar to be reboot by software
            // drv->reset();
            return false;
        }
        else
        {
            return true;
        }
    }
    else
    {
        fprintf(stderr, "Error, cannot retrieve the lidar health code: %x\n", op_result);
        return false;
    }
}

/**
 * @brief Gère l'arrêt gracieux du programme
 * @param sig le code du signal intercepté par le programme (normalement c'est 2)
 */
void end_program(int sig)
{
    program_should_quit = true;
}

void compute_theoritical_pos(float &x, float &y, float delta_x, float delta_y)
{
    x += delta_x, y += delta_y;
}

void next_beacon_pos(float &dist, float &angle, float delta_x, float delta_y, float rotation)
{
    /*  On calcule les longueurs manquantes du triangle rectangle.
        On considère que la distance à la balise est l'hypothénuse. */
    float tx = std::sin(angle) / dist;
    float ty = std::cos(angle) / dist;
}
