# Principes SOLID

## Les cinq principes

- Single responsibility
- Open-closed
- Liskov substitution
- Interface segregation
- Dependency inversion

## Single responsibility

Le principe de responsabilité unique (SRP) également appelé `separation of concern` (SOC) est assez simple à comprendre mais souvent délicat à respecter.

- Une classe doit avoir une responsabilité unique et bien définie.
- Une classe ne doit pas avoir plus d'une responsabilité.
- Une classe doit avoir une unique raison d'être modifiée.

L'anti-pattern de ce principe est le `god object` (objet divin). Un objet qui veut tout faire lui-même.

## Open-closed

Le principe d'ouverture aux extensions et de fermeture aux modifications (OCP) impose qu'une fois une classe créée, testée et mise en production, elle ne doit plus être modifiée. Elle doit être étendue.

- Lorsque vous ajoutez une fonctionnalité à une classe, vous devez le faire via une extension, pas via une modification.

### Entreprise design pattern: Specification

Une spécification est une classe qui détermine si un certain objet correspond à certains critères.

## Liskov substitution

Une classe enfant doit conserver le comportement de sa classe parent.

## Interface segregation

Au lieu d'avoir une interface complexe avec beaucoup de méthodes différentes, créer de petites interfaces dont le rôle est bien défini.

- Ne pas intégrer trop de méthodes dans une interface.

## Dependency inversion

Classes et modules de haut niveau devraient reposer sur des abstractions et non sur des implémentations de bas niveau.
