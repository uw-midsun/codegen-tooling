<% from data import parse_can_frames %> \
<% from constants import NUM_FIELDS %> \
#pragma once

#include <stddef.h>

#include "can.h"
#include "can_ack.h"
#include "can_msg_def.h"

<% can_frames = parse_can_frames(options.filename) %> 
% for id, frame in can_frames.items():

#define CAN_TRANSMIT_${frame.msg_name}( \
    % if frame.is_critical:
      ack_ptr \
    % endif
    % for i, field in enumerate(frame.fields): 
      % if i > 0 or frame.is_critical:
        , \
      % endif
      ${field} \
    % endfor 
    ) \
    do { \
    CANMessage msg = { 0 }; \
    CAN_PACK_${frame.msg_name}(&msg \
    % for field in frame.fields: 
      , (${field}) \
    % endfor
    ); \
    can_transmit(&msg \
    % if frame.is_critical:
      , (ack_ptr) \
    % else:
      , NULL \
    % endif
    ) \
    } while(0)
% endfor