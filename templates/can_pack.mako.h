<% from data import parse_can_frames %> \
<% from constants import NUM_FIELDS %> \
#pragma once

#include "can_msg_defs.h"
#include "can_pack_impl.h"

<% can_frames = parse_can_frames(options.filename) %> 
% for id, frame in can_frames.items():

#define CAN_PACK_${frame.msg_name}(msg_ptr \
    % for field in frame.fields: 
      , ${field}_${frame.ftype} \
    % endfor 
    ) \
    can_pack_impl_${frame.ftype}((msg_ptr), CAN_DEVICE_${frame.source}, CAN_MESSAGE_${frame.msg_name}, ${frame.dlc}  \
    % for field in frame.fields:
      , (${field}_${frame.ftype}) \
    % endfor
    % for _ in range(0, NUM_FIELDS[frame.ftype] - len(frame.fields)):
      , CAN_PACK_IMPL_EMPTY \
    % endfor
    )
% endfor
