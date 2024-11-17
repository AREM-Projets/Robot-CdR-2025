HOME_TREE := rplidar_sdk

ifdef DEBUG
OUTPUT_BUILD_PREFIX =Debug
else
OUTPUT_BUILD_PREFIX =Release
endif

CXXSRC += main.cpp
C_INCLUDES += -I$(HOME_TREE)/sdk/include -I$(HOME_TREE)/sdk/src
ifdef DEBUG
CFLAGS += -g
else
CFLAGS +=
endif
LD_LIBS += -lstdc++ -lpthread -L$(HOME_TREE)/output/Linux/$(OUTPUT_BUILD_PREFIX)/ -lsl_lidar_sdk

lidar: $(CXXSRC) build_sdk
	gcc $(CFLAGS) $(C_INCLUDES) -o $@ $(CXXSRC) $(LD_LIBS)

run: lidar
	./lidar

build_sdk: rplidar_sdk
	$(MAKE) -C rplidar_sdk/sdk
