Дедлайн: 18/12/2023

1. Установить Terraform.
   `Поставил`
   ![terraform install](/HW34/screen/installterraform.PNG)
2. Написать шаблон для создания виртуальной машины в облаке.
   [terraform](/HW34/terraform_HW/main.tf)
3. Познакомиться с командами:

- terraform init

```
Инициализирует рабочий каталог, содержащий файлы конфигурации Terraform.
```

![init](/HW34/screen/terraform_init.PNG)

- terraform fmt

```
Инициализирует рабочий каталог, содержащий файлы конфигурации Terraform.
```

- terraform validate

```
Команда terraform validateпроверяет файлы конфигурации в каталоге.
Validate запускает проверки, которые проверяют, является ли конфигурация синтаксически допустимой и внутренне согласованной, независимо от любых предоставленных переменных или существующего состояния.
```

![validate](/HW34/screen/terraform_validate.PNG.PNG)

- terraform plan

```
Создает план выполнения, который позволяет вам просмотреть изменения, которые Terraform планирует внести в вашу инфраструктуру.
```

![plan](/HW34/screen/terraform_plan.PNG)

- terraform apply

```
Похож на terraform plan, но запускает наш код в работу.
```

![apply](/HW34/screen/terraform_apply.PNG)

- terraform destroy

```
Уничтажает все удаленные объекты, управляемые определенной конфигурацией Terraform.
```

![destroy](/HW34/screen/terraform_destroy.PNG)
![destroy](/HW34/screen/terraform_destroy2.PNG)

4. Создать виртуальную машину в облаке при помощи ранее созданного шаблона.

5. Поменять тип виртуальной машины (увеличить количество ресурсов) через веб консоль и выполнить terraform plan. Что предлагает сделать Terraform?
