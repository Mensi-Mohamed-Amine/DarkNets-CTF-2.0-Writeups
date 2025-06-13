# **CTF Writeup: Most Wanted (OSINT Challenge)**

## **Challenge Solution**

### **1. Objective**

Find the NCIC (National Crime Information Center) number for wanted cybercriminal "Carlos" from FBI's Most Wanted list.

### **2. Research Process**

1. Searched for "FBI most wanted cybercriminal Carlos"
2. Found NBC News article:
   ```
   https://www.nbcnews.com/technolog/fbis-most-wanted-includes-hacker-who-helped-catch-cheating-lovers-8c11551655
   ```
3. Located Carlos' profile in the article containing his NCIC number

### **3. Key Discovery**

Found Carlos' NCIC identifier in the article:

```
NCIC: W617874182
```

### **4. Flag Construction**

Following the specified format:

```
Securinets{W617874182}
```

## **Final Answer**

**Flag:**

```
Securinets{W617874182}
```

## **Key Observations**

- Challenge name "Most Wanted" directly referenced FBI listings
- NCIC numbers are unique identifiers for wanted individuals
- Article contained the exact reference needed
- Flag format matched the NCIC number pattern

**Time to Solve:** ~5 minutes

**Tools Used:**

- Web search engine
- News article analysis
- FBI Most Wanted list knowledge
