# Roleta do azar

skill id: amzn1.ask.skill.617970f5-3b21-4dd0-b8d4-43dae3c98301

---

### Updating interaction models

```
$ cd roleta-do-azar
$ ask smapi get-interaction-model 
   --skill-id  amzn1.ask.skill.617970f5-3b21-4dd0-b8d4-43dae3c98301
   --stage development 
   --locale pt-BR 
   > skill-package\interactionModels\custom\pt-BR.json
```

### Local <-> This repo

```
$ cd roleta-do-azar
$ git pull personal <branch>
$ git add .
$ git commit -m <message>
$ git push personal
```

### Local <-> Amazon 

```
$ cd roleta-do-azar
$ git pull origin <branch>
$ git add .
$ git commit -m <message>
$ git push origin
```

### Local -> This repo && Amazon

```
$ cd roleta-do-azar
$ git add .
$ git commit -m <message>
$ git push all
```

