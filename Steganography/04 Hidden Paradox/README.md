# **CTF Writeup: Hidden Paradox (Metadata & Steganography Challenge)**

  

## **Challenge Overview**

  

We were given a PNG image named "Hidden Paradox.png" with dimensions 2000x2000 pixels. The challenge combined **metadata analysis** and **password-protected steganography**.

  

## **Step-by-Step Solution**

  

### **1. Initial File Inspection**

  

First, I verified the file type:

  

```bash

file "Hidden Paradox.png"

```

  

Output:

  

```

Hidden Paradox.png: PNG image data, 2000 x 2000, 8-bit/color RGBA, non-interlaced

```

![Alt text](img/1.png)

  

### **2. Metadata Analysis with ExifTool**

  

I examined the image metadata for hidden clues:

  

```bash

exiftool "Hidden Paradox.png"

```

  

Key findings:

  

```

Author                          : dexter

```

  

The **Author** field contained the value "dexter", which turned out to be crucial for solving the challenge.


![Alt text](img/2.png)

### **3. Extracting Hidden Data with StegoSuite**

  

Using the author name as a potential password, I attempted extraction:

  

```bash

stegosuite extract -k dexter "Hidden Paradox.png"

```

  

Successful output:

  

```

Loading png image from /home/dexter/Desktop/Hidden Paradox.png

Extracting data...

Extracting completed

Extracted message: Securinets{UN533N_TRU7H_0F_P4R4D0X}

```


![Alt text](img/3.png)

## **Key Techniques Used**

  

1. **Metadata Inspection**

  

   - Used `exiftool` to discover the password hint in the "Author" field

   - Common practice in CTFs to hide clues in metadata

  

2. **Password-Protected Steganography**

  

   - Recognized the need for a passphrase to extract data

   - Used `stegosuite` with the discovered password

  

3. **Pattern Recognition**

   - Connected the "Hidden Paradox" challenge name with the concept of metadata hiding

   - Understood that author/creator fields often contain credentials

  

## **Lessons Learned**

  

- **Always check metadata first** - Simple tools like `exiftool` can reveal critical clues

- **Think about password sources** - Common locations include:

  - Image metadata (author, comment fields)

  - File properties

  - Challenge descriptions

- **Stego tools vary** - Different tools (`stegosuite`, `steghide`, etc.) may be needed for different challenges

  

## **Final Flag**

  

The hidden message was successfully extracted:

  

```

Securinets{UN533N_TRU7H_0F_P4R4D0X}

```

  

## **Expansion: Alternative Approaches**

  

If the initial approach hadn't worked:

  

1. Try common passwords (admin, password, secret, etc.)

2. Use `strings` command to look for embedded clues

3. Check LSB steganography if password extraction fails

4. Examine the image in a hex editor for unusual patterns

  

This challenge effectively demonstrated how real-world data might be hidden using multiple layers of concealment.
