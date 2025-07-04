# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## 1. Required evidence

### 1.1. Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### 1.2. Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

![Sample](screenshots/sample.png)
> Note the `!`, and the use of a relative path.

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### 1.3. Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### 1.4. Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## 2. Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### 2.1. Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Local Execution (screenshot1.png)](screenshots/screenshot1.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### 2.2. Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name       | value          |
   | ----------              | ---------- | -------------- |
   | built-in primitive type | dimmed     | True 	   |
   | built-in composite type | list       | self.pixels    |
   | user-defined type       | smiley     | Smiley         |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                    |
   | ------------             | ----------------------- |
   | self.pixels              | list                    |
   | A member of self.pixels  | tuple                   |
   | self                     | object                  |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File       | First line 		     | Line range  |
   | ------------ | ---------- | --------------------------- | ----------- |
   |  sequence    | smiley.py  | self.sense_hat = SenseHat() | 13-26       |
   |  selection   | sad.py     | eyes = [10, 13, 18, 21]     | 24-30       |
   |  iteration   | sad.py     | def draw_mouth(self):       | 16-22       |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example              |
   | ----------------------- | ----- | ---------------------|
   | int                     | Yes   | mouth = [49, 54, 42, 43, 44]    |
   | float                   | Yes   | dimming_factor = 0.6 |
   | str                     | No    | None         	    |
   | bool                    | Yes   | dimmed=True          |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

| Variable Type      | Example               | Explanation                                                                                   |
|--------------------|-----------------------|-----------------------------------------------------------------------------------------------|
| Class variable     | `WHITE = (255, 255, 255)` | This is a class variable defined once in the class and it acts as a constant shared by all instances. |
| Instance variable  | `self.pixels`         | This instance variable is created in `__init__` and holds data unique to each object instance.    |


6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

- Generally, the constructor __init__ intialises a new object's attributes and prepares it for use
- In happy.py it calls super().__init___() to setup the Smiley class and then runs the simulated happy mouth and eyes


   2. What statement(s) does it execute (consider the `super` call), and what is the result?

- In happy.py, from Line 11 - the constructor call runs the code:

```python
6. class Happy(Smiley, Blinkable):
7.     """
8.     Provides a Smiley with a happy expression
9.     """
10.    def __init__(self):
11.        super().__init__()
12.
13.        self.draw_mouth()
14.        self.draw_eyes()
```


### 2.3. Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:

- The python code is using style from PEP 8 which is Python's official style guide. SenseHat is using the same python format.

2. List three aspects of this convention you see applied in the code.

  1. Uses indentation consitently
  2. Constants are written in UPPERCASE
  3. Variables are snake_case

4. Give two examples of organizational documentation in the code.

 1. Inline comments with:  # Give the process some time to start
 2. Docstrings describing a function: """Updates the GUI using a queue for communication with the main process."""

### 2.4. Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.

  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s)     |
|------------|---------------|----------------------|
| Smiley     | Super         | SenseHat             |
| Sad        | Sub           | Smiley               |
| Happy      | Sub           | Smiley, Blinkable    |
| Blinkable  | Sub           | ABC                  |


2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

- Abstraction means showing only what’s needed and hiding the complicated parts. In this project, the Smiley class hides the details of how the LED display works—so instead of setting pixels manually, you just call methods like draw_eyes() to make a face.

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

- Inheritance - this means creating new classes (i.e. Happy and Sad) that get features from another class (Smiley). This way, Happy and Sad don’t have to rewrite common code—they - they just change what is needed to make the Happy and Sad code unique.

### 2.5. Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
- Happy = gets/inherits from Smiley and Blinkable, and blinks
- Sad = gets/inherits from only Smiley which is wide open or shut - no blinks
   
3. What are the key similarities?
   Happy + Sad both inherit from Smiley
   
4. What difference stands out the most to you and why?
   Blinkable - Happy has blinkable, and I think the Blink sequence is a friendly guesture from the code to me.
   
5. How does this difference affect the functionality of these classes
   The functionaility means Happy will blink, Sad will not.
   

### 2.6. Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
- The class Smiley encapsulates the SenseHat object so any subclass that has Smiley will also get the functionality.
   
2. Which of these classes directly interact with the SenseHat functionalities?
- The class Smiley in smiley.py def __init__(self) has self.sense_hat = SenseHat(), and is defined in functions show() and dim_display().
   
4. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words) 
- Encalpsulation hides the details of interacting with the SenseHat inside the Smiley class. smiley.py only provides out dim_displayed
and show. This means that only required code is needed to refresh, minimsing complexity of the code.
   

### 2.7. Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.
- I assume, without contacting the code's author that only Happy should blink, as Blinkable is only in the class Happy. If the author
  wanted all Smiley to blink, Blinkable would be with the Super - class Smiley.

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.
- No, because the subclass can change the way it blinks. A subclass can differ the blinking behaviour.

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.
- Polymorphism allows different classes to provide their own version of a class method that is in the parent class.

4. How is inheritance used in the blink method, and why is it important for polymorphism?
- Inheritance allows a subclass to have their own version of the blink method, meaning it can be customised. This allows different smiles to react differently while using the same name.

1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):  # Implement Blink in Sad class
        """
        Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
    ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](screenshots/sad_blinking.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > Sad smiley now blinks at me too. Adjustments included substituting sad/Sad in happy/Happy and settings the function to blink.

  ### 2.8. If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > Blinkable is an ABC - Abstract Base Class - and inherits the function of blink() to be used in subclass.

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > Interface

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > Abstraction. Blinkable defines that blink() exists and how it works, without Blinkable it won't work. With blinkable it does the code without the developer having to re-create it.

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > Python allows classes to define their own methods. The Sad class can implement a blink() without need to inherit Blinkable. As it is already called in the code.

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > duck typing. Quack. If an object is setup it can be used without specific inheritance and can be used but changed in another part of the code. Basically if upstream quacks, we can be a duck. Not the same duck, a different duck that quacks.

  ***

  ## 3. Refactoring

  ### 3.1. Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > class Smiley has WHITE GREEN RED YELLOW AND BLANK
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > Tuples as it represents the colours from (R, G, B) i.e. GREEN = (0, 255, 0) 
     3. Add the color blue to the appropriate class using the appropriate format and values.
        > BLUE = (0, 0, 255)

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > The colour variables defined in class Smiley are used in Smiley and subclasses that call it such as Happy and Sad and they
        set pixel colours for different functions.

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Simplest would be to specify green RGB code in YELLOW. YELLOW = (0, 255, 0) - this is not the best as its a contriction between
     a name and actual.

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### 3.2. Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.
 > Done

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.
  > Done

  4. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.
  > I considered that Abstraction best applies as it allows it to be changed without specifying a color.

  5. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.
  > Confirmed

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### 3.3. Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.
 >     def __init__(self, complexion=YELLOW): # Default complexion is yellow

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.
>     Changed self.YELLOW to self.my_complexion 

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.
> Agree - this avoid conflicts with complexion as my_complexion is unique, so there will be no confusion in the code.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### 3.4. Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.
  - Yes it does.
    
  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.
  - Yellow blinky face still there too.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.
  - Created angry.py
  ***
