<% from data import parse_can_frames %> \
<% from constants import NUM_FIELDS, NUM_DLC_BYTES %> \
#pragma once

#include "can_msg_def.h"
#include "can_pack_impl.h"

<% can_frames = parse_can_frames(options.filename) %> 
% for id, frame in can_frames.items():

#define CAN_PACK_${frame.msg_name}(msg_ptr \
    % for field in frame.fields: 
      , ${field} \
    % endfor 
    ) \
    can_pack_impl_${frame.ftype}((msg_ptr), ${frame.source}, ${frame.msg_name}, \
        ${int(len(frame.fields) * NUM_DLC_BYTES / max(1, NUM_FIELDS[frame.ftype]))}  \
    % for field in frame.fields:
      , (${field}) \
    % endfor
    % for _ in range(0, NUM_FIELDS[frame.ftype] - len(frame.fields)):
      , CAN_PACK_IMPL_EMPTY \
    % endfor
    )
% endfor
