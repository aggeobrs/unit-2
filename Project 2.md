# **Computer Science - Project 2**

By Angelos & Paula


**TASK**

Design and implement a multisensorial counter (0-9) for a client that does not know the roman numbers. It should allow the user to count up and down from a set start.

## **Criterion A: Planning**

**Problem definition:**

We need to design and implement a multisensorial counter that can count from 0 to 9 up and down from a set number. The client doesn’t know the roman numbers and has a disability. 
The product is being developed because it is important to be inclusive with everyone and we all have the right to be able to count from 0 to 9. There are many similar products that allow disabled users to count numbers, such as watches, traffic lights etc.

**Proposed Solution:**

**Design statement:**

We will design and implement a multisensorial counter (0-9) for a client that does not know the roman numbers. Specifically, the numbers from 0 to 9 will be presented with light and with sound. So everyone, including disabled people will be able to receive the information. The program will be based on binary code and is constructed using the software Python 3.0. It will take 3 weeks to make and will be evaluated according to the criteria A Planning, B Solution Overview, and C Development.

What is the personal relevance of the program? Why did you pick the theme?
We want to be inclusive and give opportunities to everyone. So, it is important that all people in the world have access to counting methods. Everyone has the right to have a counter, it shouldn’t matter having a disability. 
That is why we included light bulbs and sound, so that everyone will be able to understand it.
We chose a mix of binary and morse code for our counting system because it can be understandable for all and we personally like the idea of reading lines ( - ) and dots ( · ), as some spies and special forces.

**Justify the software selected:**

Python is one of the most accessible programming languages because it is not complicated and has simplified syntax very similar to the English language, which is perfect for beginners. According to PYPL and ZDNet [^1], [^2], Python is one of the most popular languages with about 30% of programmers use Python as their main programming language, so there is a big Internet community to ask for help. Also, its codes can be easily written and executed much faster than other programming languages. Python is an open source and has a lot of  tools, like functions or libraries to complement the code, so you can do practically anything with your code. It is also friendly for the programmers and the users, making it possible to be read even by people who are not programmers. It is easy to implement data structures in Python with built-in insert, append functions. Also, there is a large library of built-in functions in Python.
Finally, we will use an online conversor from Python to C so we can use our program in Arduino. 

[^1]: Tung, Liam. “Programming Languages: Python Just Took a Big Jump Forward.” ZDNet, ZDNet, 6 Oct. 2021, https://www.zdnet.com/article/programming-languages-python-just-took-a-big-jump-forward/

[^2]: “PYPL Popularity of Programming Language Index.” Index, https://pypl.github.io/PYPL.html

**Justify the structure of the proposed solution:**

Our program has the typical type and it is easy to understand. There are comments on each step, so someone who reads the code can understand easily what is happening. Also, there are functions that make the code simple and variables with names that are understandable.

**Success Criteria**

- The counter has to count from 0 to 9, upwards and downwards.
- All digits (0-9) will be presented with light and sound at the same time
- Dots ( · ) will be represented with a light bulb and a sound that last 0.4 seconds, while the lines ( - ) will be represented with a light bulb and a sound that last 1 second.


## **CRITERION B**

![image](https://user-images.githubusercontent.com/89012983/146902489-a99b37ba-1dd0-48e9-a512-21c3eadd3951.png)

This table represents a conversion from decimal numbers to binary numbers, which then are converted to our own system where:
Dots ( · ) will be represented with a light bulb and a sound that last 0.5 seconds.
Lines ( - ) will be represented with a light bulb and a sound that last 3 seconds.

**System diagram**

![image](https://user-images.githubusercontent.com/89012983/146902828-bb1133da-18c9-40ec-b481-b43c687befe3.png)

Figure 2: System diagram of the proposed solution

This is the System Diagram. You can see how the program is operated in a computer HP with its specifications, with the operating system of Windows 10. The programme used to run this project is PyCharm Edu and the archive's name is counter.py. The code asks the user to input the starting number and to decide if they want to count downwards or upwards. Then, it processes the data and finally outputs sound and light to represent the numbers. 

**Test Plan**

![image](https://user-images.githubusercontent.com/89012983/146903193-27090603-efdf-4597-ae2a-1aefe8b33142.png)

This is a list of steps, table, or flow chart specifying the process for testing the solution with the inputs and expected outputs.

**3 FLOW DIAGRAMS or K-maps and logic circuits for algorithms**

![image](https://user-images.githubusercontent.com/89012983/146903574-7e2b819c-a276-4b8d-8748-b9fd9ac78422.png)

Fig 3: Flow diagram 1 showing the counter upwards or downwards\

![Flow diagram 2](https://user-images.githubusercontent.com/89012983/146903901-22bb62a6-cbd2-492c-802c-ab563a9390e5.jpg)

Fig 4: Flow diagram 2 showing the counter upwards or downwards with a starting number

![Flow diagram 3](https://user-images.githubusercontent.com/89012983/146903851-2f77a107-a28d-4e9d-9105-cb114004fc15.jpg)

Fig 5: Flow diagram 3 showing the counter in Binary Morse system upwards or downwards

**Record of Tasks**

| Task No |                           Planned Action                          |                                          Planned Outcome                                         | Time estimate | Target completion date |    Criterion    |
|:-------:|:-----------------------------------------------------------------:|:------------------------------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------------:|
| 1       | Write problem definition, proposed solution and success criteria. | For having clear ideas about the project, the design, the software and the goals.                |     40min     |          Dec 8         |   A - Planning  |
| 2       | Create system diagram                                             | To have a clear idea of the hardware and software requirements for the proposed solution.        |     10min     |          Dec 9         |    B - Design   |
| 3       | Create flow diagrams                                              | To have clear ideas on how to code and how the programme would work.                             |     40min     |         Dec 14         |    B - Design   |
| 4       | Think about test plan                                             | For having clear goals and what to expect.                                                       |     10min     |         Dec 14         |    B - Design   |
| 5       | Code the base of the program                                      | There are different python codes for our program.                                                |     30min     |         Dec 14         | C - Development |
| 6       | Make some improvements in the code                                | General improvements.                                                                            |       1h      |         Dec 15         | C - Development |
| 7       | Improve user intuitive instructions                               | Change some codes so it is easier to the user to understand the game, based on the previous test |     20min     |         Dec 15         | C - Development |
| 8       | Write tools and techniques used in the program                    | So they can be accessible all time and anyones knows the resources used.                         |     30min     |         Dec 15         | C - Development |
| 9       | Convert Python code to C and Arduino                              | Arduino Tinkercad uses C language for running its programs so we have converted our Python code. |       1h      |         Dec 17         | C - Development |
| 10      | Make some improvements in the Arduino code                        | Adding light and sound and changing their duration                                               |       2h      |         Dec 18         | C - Development |
| 11      | User interface sketch                                             | Photo of Arduino as the user interface sketch                                                    |      5min     |         Dec 18         |    B - Design   |

**User Interface Sketch**

![image](https://user-images.githubusercontent.com/89012983/146904581-9b457ec2-f66e-4d30-a267-0dd7b299ad89.png)

Fig 6: Arduino webpage with our program

## **CRITERION C**

**Existing tools**

- Python
- C Language
- Converter from Python to C Language [^3] 
- Arduino Platform [^4]
- GitHub [^5]

[^3]: https://pythoncsharp.com/
[^4]: https://www.tinkercad.com/dashboard
[^5]: https://github.com/

**List of techniques used**

- **Variables:**
Variables are used for storing values as if the user wants to go upwards or downwards and the number he will start counting.
- **Conditions: If, elif, else statements:**
With the if, elif and else statements we make sure that there are not incorrect values given by the user in the variables. Then we use them to run our program correctly.
- **While loops:**
We use the while loops to create a repetition of instructions and to make sure all the correct numbers are shown.
- **For loops:**
We use the while loops to create a repetition of instructions during a concrete time.
- **Input instruction:**
We use this to create variables by an instruction given by the user. 
- **Print instruction:**
We use the print instruction to give messages to the user and show the result of the counting.
- **Data Encoding:**
Computers use data encoding to store and retrieve meaningful information as data.
- **Functions:**
Modules of code to run when it’s convenient and do a specific task inside the program.

**Development**

```.ino
char nums[10][5] = {"0000","0001","0010","0011","0100","0101","0110","0111","1000","1001"};


#define joystick  A0 // Arduino pin connected to VRX pin

int xValue = 0; // To store value of the X axis

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);	// led
  pinMode(7, OUTPUT); 			// buzzer

  Serial.begin(9600);
  Serial.println("Hello. Starting system");
}

void loop()
{
  
  
  // pot
  // read analog X and Y analog values
  xValue = analogRead(joystick);

  // print data to Serial Monitor on Arduino IDE
  Serial.print("x = ");
  Serial.println(xValue);
 
 
  if(xValue>511){
    
	// upwards
    int a = 0;
    while (a < 9){
      a += 1;
      Serial.println(a);
      visu(nums[a]);
      delay(1500);
    }
   
  }else{
    
  	// downwards
    int a = 10;
  	while (a > 1){
    	a -= 1;
        Serial.println(a);
        visu(nums[a]);
      	delay(1500);
    }
 
  }
  
}

void line()
{
  digitalWrite(LED_BUILTIN, HIGH);
  tone(7, 220, 1000);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}

void dot()
{
  digitalWrite(LED_BUILTIN, HIGH);
  tone(7, 220, 400);
  delay(400);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}



// n is an element of the array nums, i.e. "0001"
void visu(char *n)
{
  for (int i = 0; i < 4; i++) {
    if (n[i] == '0') {
      dot();
    } else {
      line();
    }
  }
}

```

Fig 7: Counter upwards or downwards using light and sound

To solve the first criterion in the clients requirement I decided to create a binary counter shown in Fig. 7. Using pattern recognition I build a program with for and while loops, conditions, variables and functions. Also, some instructions especially created for the Arduino machine are used.
