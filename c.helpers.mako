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
