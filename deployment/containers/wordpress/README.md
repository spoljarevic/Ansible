## Deploying Wordpress inside a container ##

### What you can use? ###
I created two nearly identical Playbooks, one for Docker and one for Podman.
They are both not tested yet but should in theory work fine.

I prefer Podman but thought I'd give you a choice.

### What needs to be changed before running? ###
Both Playbooks use the same variables, just change them so something you prefer or is more secure.

**Wordpress**
First you can/should change the port of the wordpress container to something that is more secure or at least available.
```
ports:
    - "8080:80"
```

Just change the ``8080`` and you'll be fine.

Then you'd need to change the env part.
```
env:
    WORDPRESS_DB_HOST: db
    WORDPRESS_DB_USER: exampleuser
    WORDPRESS_DB_PASSWORD: examplepass
    WORDPRESS_DB_NAME: exampledb
```
Those need to be changed for security reasons!

**MYSQL**
Same as on wordpress, you'll need to change the env part.
```
env:
    MYSQL_DATABASE: exampledb
    MYSQL_USER: exampleuser
    MYSQL_PASSWORD: examplepass
    MYSQL_RANDOM_ROOT_PASSWORD: "1"
```

Please make sure that those match the ones you set for wordpress since they need to match in order to connect.

Now you're good to go, enjoy deploying!
