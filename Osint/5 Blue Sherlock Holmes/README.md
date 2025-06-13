# **CTF Writeup: Blue Sherlock Holmes (OSINT Challenge)**

## **Challenge Solution**

### **1. Objective**

Find Dexter's BlueSky (formerly Twitter) account using the Sherlock username search tool.

### **2. Tool Execution**

Ran Sherlock to scan for "dexter" username across platforms:

```bash
sherlock dexter
```

### **3. Key Finding**

Among 244 results, discovered the BlueSky account:

```
Bluesky: https://bsky.app/profile/dexter.bsky.social
```

### **4. Flag Construction**

Following the specified format:

```
Securinets{https://bsky.app/profile/dexter.bsky.social}
```

## **Final Answer**

**Flag:**

```
Securinets{https://bsky.app/profile/dexter.bsky.social}
```

## **Key Observations**

- Challenge name hinted at using Sherlock tool ("Blue Sherlock Holmes")
- "Blue" referred to BlueSky platform
- Username search revealed account among many results
- Flag format required full URL encapsulation

**Time to Solve:** ~3 minutes

**Tools Used:**

- Sherlock OSINT tool
- Basic command line
