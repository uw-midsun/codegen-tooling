<%doc>
Helps generating enum body content in the format:

    prefix_val0 = 0,
    prefix_val1,
    prefix_val2,
    NUM_prefix
    ...

Args:
    data: a dictionary of data in the range (empty values should have a value of None)
    prefix: the prefix to use for final/dummy elements
</%doc>
<%def name="generate_enum(data, prefix)">
  <% dummy_count = 0 %>
  % for key, value in data.items():
    % if value != None:
      % if key == 0:
        ${value} = 0,
      % else:
        ${value},
      % endif
    % else:
      ${prefix}_DUMMY_${dummy_count},
    % endif
    <% dummy_count = dummy_count + 1 %> \
  % endfor
  NUM_${prefix} 
</%def>
