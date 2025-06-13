# **CTF Writeup: HackConcordia (OSINT Challenge)**

## **Challenge Solution**

### **1. Instagram Profile Investigation**

1. Visited the Instagram profile: [HackConcordia](https://www.instagram.com/HackConcordia)
2. Examined the bio section which contained a link

### **2. Link Analysis**

1. The bio link directed to: [Event Website URL](https://linktr.ee/HackConcordia?fbclid=PAZXh0bgNhZW0CMTEAAadMwuZzVw8SQRgumkh0vr9mzr1hCTTrr1z7pb5BxHNoFHd_KA_8hPn91Mp_XQ_aem_3y14yeyNWuKsWKBw-Nq-Yw)
2. Found the following key dates on the website:
   - Event Start: 01 February 2025
   - Event End: 02 February 2025

### **3. Flag Construction**

Using the date format specified in previous flags:

```
Securinets{01_February_2025_To_02_February_2025}
```

## **Key Steps**

1. **Profile Examination** - Located the bio link
2. **Website Analysis** - Identified event dates
3. **Flag Formatting** - Applied consistent date format

## **Final Answer**

**Flag:**

```
Securinets{01_February_2025_To_02_February_2025}
```

## **Tools Used**

1. Instagram Web
2. Browser Developer Tools (for link analysis)
3. Date formatting validator

## **Time to Solve:** ~5 minutes

**Note:** This challenge demonstrates how event information in social media bios can contain hidden flags when properly formatted.
