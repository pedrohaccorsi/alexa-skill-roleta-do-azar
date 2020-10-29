# Roleta do azar

skill id: amzn1.ask.skill.617970f5-3b21-4dd0-b8d4-43dae3c98301

---

### Setting the remotes 

##### Amazon

```
$ origin  https://git-codecommit.us-east-1.amazonaws.com/v1/repos/617970f5-3b21-4dd0-b8d4-43dae3c98301 (fetch)
$ origin  https://git-codecommit.us-east-1.amazonaws.com/v1/repos/617970f5-3b21-4dd0-b8d4-43dae3c98301 (push$ )
```

##### Personal

```
$ git remote add personal https://github.com/pedrohaccorsi/alexa-skill-roleta-do-azar.git 
$ git remote set-url --add --push personal https://github.com/pedrohaccorsi/alexa-skill-roleta-do-azar.git
```

##### Both together
```
$ git remote add all https://git-codecommit.us-east-1.amazonaws.com/v1/repos/617970f5-3b21-4dd0-b8d4-43dae3c98$ 301
$ git remote set-url --add --push all https://git-codecommit.us-east-1.amazonaws.com/v1/repos/617970f5-3b21-4d$ d0-b8d4-43dae3c98301
$ git remote set-url --add --push all https://github.com/pedrohaccorsi/alexa-skill-roleta-do-azar.git$ 
```



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

