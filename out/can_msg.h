#pragma once

// For setting the CAN device
typedef enum {

  CAN_DEVICE_PLUTUS = 0,
  CAN_DEVICE_CHAOS = 1,
  CAN_DEVICE_TELEMETRY = 2,
  CAN_DEVICE_LIGHTS = 3,
  CAN_DEVICE_MOTOR_CONTROLLER = 4,
  CAN_DEVICE_THEMIS = 5,
  CAN_DEVICE_RASPBERRY_PI = 6,
  CAN_DEVICE_MPPT_FRONT = 7,
  CAN_DEVICE_MPPT_REAR = 8,
  NUM_CAN_DEVICE = 9
} CanDevice;

// For setting the CAN message ID
typedef enum {

  CAN_MESSAGE_BPS_FAULT = 0,
  CAN_MESSAGE_MOTOR_DRIVE = 1,
  CAN_MESSAGE_MOTOR_CRUISE = 2,
  CAN_MESSAGE_CHANGE_TURN_SIGNAL_STATE = 3,
  CAN_MESSAGE_HAZARD = 4,
  CAN_MESSAGE_HEADLIGHT_STATE = 5,
  CAN_MESSAGE_BRAKE_LIGHT_STATE = 6,
  CAN_MESSAGE_HORN_STATE = 7,
  CAN_MESSAGE_SET_BUS_CURRENT_LIMIT = 8,
  CAN_MESSAGE_HEARTBEAT_REQUEST = 9,
  CAN_MESSAGE_SET_POWER_STATE = 10,
  CAN_MESSAGE_THROTTLE_POSITION = 11,
  CAN_MESSAGE_MECHANICAL_BRAKE_POSITION = 12,
  CAN_MESSAGE_BATTERY_MODULE_VOLTAGE = 13,
  CAN_MESSAGE_BATTERY_CURRENT = 14,
  CAN_MESSAGE_BATTERY_MODULE_TEMPERATURE = 15,
  CAN_MESSAGE_BATTERY_STATE_OF_CHARGE = 16,
  CAN_MESSAGE_SOLAR_VOLTAGE = 17,
  CAN_MESSAGE_SOLAR_POWER = 18,
  CAN_MESSAGE_SOLAR_CURRENT = 19,
  CAN_MESSAGE_MOTOR_SPEED = 20,
  CAN_MESSAGE_MOTOR_CURRENT = 21,
  CAN_MESSAGE_MOTOR_VOLTAGE = 22,
  CAN_MESSAGE_HEARTBEAT_RESPONSE = 23,
  CAN_MESSAGE_POWER_RAIL_CHANGE = 24,
  CAN_MESSAGE_AUX_BATTERY_STATE = 25,
  NUM_CAN_MESSAGE = 26
} CanMessage;
