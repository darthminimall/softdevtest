# Computer Inventory System
## Introduction
This piece of software is a simple Django application using Postgres and the
builtin Django ORM for inventory management for computers. It is being written
as part of an application to the Rensselaer Union.

An inventory entry contains:
* Manufacturer
* Serial Number
* Comments

A user should be able to:
* Create multiple "inventories" (like folders, can be given arbitrary but
  unique names).
* Within an inventory, users can add, modify, or delete an entry for a given
  computer.

This project also makes use of Bootstrap.

## Specification
### Model
The model consists of the following two objects:
* __Inventory Object__
  * Field for inventory name of type CharField(max\_length=100)
* __Computer Object__
  * Field for inventory of type ForeignKey(Inventory)
  * Field for manufacturer of type CharField(max\_length=50)
  * Field for serial number of type CharField(max\_length=50)
  * Field for comments of type TextField()

### Views
* A view to access a list of inventories (the default view)
* A view to access a list of computers in inventories.
* A view to add inventories
* A view to add computers
* A view to delete computers
* A view to modify computers
