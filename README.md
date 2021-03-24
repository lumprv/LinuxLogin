# LinuxLogin

This is a simple program that stimulates the login process in Linux systems.

It prompts you for a username and password of a user profile. 
Then, it is checked against ***etc/shadow file*** if it matches with typed credentials or not.

User has three attempts to guess the correct credentials.

The code should be run as *sudo* to have permission to read from shadow file.

#### Caution 

This program was created for educational purposes only.  It's not good practice to have numerous people knowing and using the root password because when logged in as root, you can do anything to the system. This could provide too much power for inexperienced users, who could unintentionally damage the system.
