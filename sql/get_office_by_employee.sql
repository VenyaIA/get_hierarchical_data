-- Находим id и name офиса, где работает сотрудник, фильтруем только данные об офисе через type = 1
with recursive employee_to_office as (
  select
    employee.*
  from
	organization_structure employee
  where
	employee.id = %s
  union all
  select
	parent.*
  from
	organization_structure parent
	, employee_to_office eto
  where
	eto.parent_id = parent.id
)
select
  id, name
from
  employee_to_office
where
  type = 1