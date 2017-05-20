<%doc>
Helps generating enum body content in the format:

    prefix_val0 = 0,
    prefix_val1 = 2,
    prefix_val2 = 5,
    NUM_prefix
    ...

Args:
    data: a dictionary of data in the range (empty values should have a value of None)
    prefix: the prefix to use
</%doc>
<%def name="generate_enum(data, prefix)"> \
  % for key, value in data.items():
    % if value != None:
      ${prefix}_${value} = ${key},
    % endif
  % endfor
  NUM_${prefix} = ${len(data)} \
</%def>
