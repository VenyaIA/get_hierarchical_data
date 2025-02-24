-- Находим имена всех сотрудников офиса, через фильтрацию по type = 3 (сотрудники)
with recursive office_employees as (
  select
	parent.*
  from
	organization_structure parent
  where
	parent.id = %s
  union all
  select
	employee.*
  from
	organization_structure employee
	, office_employees oe
  where
	  oe.id = employee.parent_id
)
select
  name
from
  office_employees
where
  type = 3