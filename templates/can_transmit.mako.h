<% from data import parse_can_frames %> \
<% from constants import NUM_FIELDS %> \
#pragma once

#include <stddef.h>

#include "can.h"
#include "can_ack.h"
#include "can_msg_def.h"

<% can_frames = parse_can_frames(options.filename) %> 
% for id, frame in can_frames.items():

#define CAN_TRANSMIT_${frame.msg_name}(msg_ptr \
    % if frame.is_critical:
      , ack_ptr \
    % endif
    ) \
    can_transmit((msg_ptr) \
    % if frame.is_critical:
      , (ack_ptr) \
    % else:
      , NULL \
    % endif
    ) 
% endfor
