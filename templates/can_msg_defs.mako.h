<%namespace name="helpers" file="/helpers/helpers.mako" /> \
<% from data import NUM_CAN_MESSAGES, NUM_CAN_DEVICES, parse_can_device_enum, parse_can_message_enum, parse_can_frames %> \
#pragma once

#include <stdbool.h>

#include "can_msg.h"

// For setting the CAN device 
typedef enum { 
  <% can_devices = parse_can_device_enum() %> \
  ${helpers.generate_enum(can_devices, 'CAN_DEVICE')}
} CanDevice;

// For setting the CAN message ID
typedef enum {
  <% can_messages = parse_can_message_enum(options.filename) %> \
  ${helpers.generate_enum(can_messages, 'CAN_MESSAGE')}
} CanMessage;

% for _, dev_name in can_devices.items():
#define CAN_MSG_ACK_DEVICE_${dev_name} 1 << CAN_DEVICE_${dev_name}

% endfor

<% can_frames = parse_can_frames(options.filename) %> \
#define CAN_MSG_IS_CRITICAL(msg_ptr) \
  ( \
  % for id, frame in can_frames.items():
    % if frame.is_critical:
      (msg_ptr)->msg_id == CAN_MESSAGE_${frame.msg_name} || \
    % endif
  % endfor
  false)


