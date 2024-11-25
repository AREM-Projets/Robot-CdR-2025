/*
 * Mouvement3Roues.h
 *
 *  Created on: May 1, 2024
 *      Author: Kezia
 */

#ifndef INC_EMBASE3ROUES_HPP_
#define INC_EMBASE3ROUES_HPP_

#include "main.h"
#include <stdint.h>

#include "BlocMoteurs.hpp"
#include "config.hpp"

// degueulasse
extern UART_HandleTypeDef huart2;

extern volatile bool motors_busy;
extern volatile bool movement_allowed;
//pour l'init
extern volatile bool get_out_step;
//Deplacement absolut



enum TaskType_t
{
	NONE,
	WAIT,
	MOVE_RELATIVE,
	MOVE_SPEED,
	UART_SEND
};

struct Task_t
{
	TaskType_t type;

	// Type : movement (relative or not...)
	double x;
	double y;
	double theta;

	// Type : wait
	uint32_t delay_ms;

	// Type : UART Send
	uint8_t c;
};

class Embase3Roues : public BlocMoteurs
{
public:
	using BlocMoteurs::BlocMoteurs;
	void init();

	int32_t appendSpeedMove(double vx, double vy, double wz);
	int32_t appendRelativeMove(double x, double y, double theta);
	int32_t appendWait(uint32_t delay_ms = 0);
	int32_t appendUart(uint8_t c);


	int32_t insertRelativeMove(double x, double y, double theta);
	int32_t insertWait(uint32_t delay_ms = 0);
	int32_t insertUart(uint8_t c);

	TaskType_t executeInstruction();

	int32_t getCurrentIndex();
	TaskType_t getCurrentType();

private:
	Task_t _task_buffer[MAX_TASK_COUNT];
	int32_t _last_index = 0;

	int32_t _current_index = 0;

	int32_t appendInstruction(Task_t task);
	int32_t insertInstruction(Task_t task);

	// Movement related, used by moveRelative()

	void setStep(double x, double y, double theta);
	void translate(double x, double y);
	void rotate(double theta);

	// Functions linked to tasks
	void moveSpeed(double vx, double vy, double wz);
	void moveRelative(double x, double y, double theta);
	void wait(uint32_t delay_ms);
	void stop(void);
};

void copyTask(Task_t &dest, Task_t &src);
void initTask(Task_t &task);

#endif /* INC_EMBASE3ROUES_HPP_ */
