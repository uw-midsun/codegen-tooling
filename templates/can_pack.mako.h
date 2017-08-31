<% from data import parse_can_frames %> \
<% from constants import NUM_FIELDS %> \
#pragma once

#include "can_msg_def.h"
#include "can_pack_impl.h"

#define FIELD_UNUSED 0

<% can_frames = parse_can_frames(options.filename) %> 
% for id, frame in can_frames.items():

#define CAN_PACK_${frame.msg_name}(msg_ptr \
    % for field in frame.fields: 
    , ${field} \
    % endfor 
    ) \
    can_pack_impl_${frame.ftype}((msg_ptr), ${frame.source}, ${frame.msg_name} \
    % for field in frame.fields:
       , (${field}) \
    % endfor
    % for _ in range(0, NUM_FIELDS[frame.ftype] - len(frame.fields)):
       , FIELD_UNUSED \
    % endfor
    )
% endfor
