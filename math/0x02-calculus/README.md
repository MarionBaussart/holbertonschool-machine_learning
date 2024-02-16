# 0x02-calculus

## 0. Sigma is for Sum
![Getting Started](https://latex.codecogs.com/gif.latex?\sum_{i=2}^{5}&space;i)
= 2 + 3 + 4 + 5

## 1. The Greeks pronounce it sEEgma
![Getting Started](https://latex.codecogs.com/gif.latex?\sum_{k=1}^{4}&space;9i&space;-&space;2k)
= 36i -20

## 2. Pi is for Product
![Getting Started](https://latex.codecogs.com/gif.latex?\prod_{i&space;=&space;1}^{m}&space;i)
= m!

## 3. The Greeks pronounce it pEE
![Getting Started](https://latex.codecogs.com/gif.latex?\prod_{i&space;=&space;0}^{10}&space;i)
= 0

## 4. Hello, derivatives!
![Getting Started](https://latex.codecogs.com/gif.latex?\frac{dy}{dx}) where ![Getting Started](https://latex.codecogs.com/gif.latex?y&space;=&space;x^4&space;+&space;3x^3&space;-&space;5x&space;+&space;1)
= ![Getting Started](https://latex.codecogs.com/gif.latex?4x^3&space;+&space;9x^2&space;-&space;5)

## 5. A log on the fire
![Getting Started](https://latex.codecogs.com/gif.latex?\frac{d&space;(xln(x))}{dx}) = ![Getting Started](https://latex.codecogs.com/gif.latex?ln(x)%20+%201)

## 6. It is difficult to free fools from the chains they revere
![Getting Started](https://latex.codecogs.com/gif.latex?\frac{d&space;(ln(x^2))}{dx}) = ![Getting Started](https://latex.codecogs.com/gif.latex?\frac{2}{x})

## 7. Partial truths are often more insidious than total falsehoods
![Getting Started](https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial&space;y}&space;f(x,&space;y)) where ![Getting Started](https://latex.codecogs.com/gif.latex?f(x,&space;y)&space;=&space;e^{xy}) and ![Getting Started](https://latex.codecogs.com/gif.latex?\frac{\partial&space;x}{\partial&space;y}=\frac{\partial&space;y}{\partial&space;x}=0)

![Getting Started](https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial&space;y}&space;f(x,&space;y)) = ![Getting Started](https://latex.codecogs.com/gif.latex?xe^{xy})

## 8. Put it all together and what do you get?
![Getting Started](https://latex.codecogs.com/gif.latex?\frac{\partial^2}{\partial&space;y\partial&space;x}(e^{x^2y})) where ![Getting Started](https://latex.codecogs.com/gif.latex?\frac{\partial&space;x}{\partial&space;y}=\frac{\partial&space;y}{\partial&space;x}=0)

![Getting Started](https://latex.codecogs.com/gif.latex?\frac{\partial^2}{\partial&space;y\partial&space;x}(e^{x^2y})) = ![Getting Started](https://latex.codecogs.com/gif.latex?2x(1+x^2y)e^{x^2y})

## 9. Our life is the sum total of all the decisions we make every day, and those decisions are determined by our priorities
Write a function ``def summation_i_squared(n):`` that calculates ![Getting Started](https://latex.codecogs.com/gif.latex?\sum_{i=1}^{n}&space;i^2):

- n is the stopping condition
- Return the integer value of the sum
- If n is not a valid number, return None
- You are not allowed to use any loops

## 10. Derive happiness in oneself from a good day's work
Write a function ``def poly_derivative(poly):`` that calculates the derivative of a polynomial:

- poly is a list of coefficients representing a polynomial
    - the index of the list represents the power of x that the coefficient belongs to
    - Example: if f(x) = x^3 + 3x +5, poly is equal to [5, 3, 0, 1]
- If poly is not valid, return None
- If the derivative is 0, return [0]
- Return a new list of coefficients representing the derivative of the polynomial

## 11. Good grooming is integral and impeccable style is a must
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/6/ada047ad4cbee23dfed8.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221206T133834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=88e78cd3d40954d8d3b0bd2d27a8f123fd66ad3b5d04197db24d74f93d73dd02) = x^4 * 1/4 + C

## 12. We are all an integral part of the web of life
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/6/9ed107b0dcdde8dd49ac.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221206T133834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8a2f68be41383e4f7c83428c4003d66c8e0b79fd92a0f32a8f420ce410c02de7)
= e(2y) * 1/2 + C

## 13. Create a definite plan for carrying out your desire and begin at once
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/6/b94ec3cf3ae61acd0275.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221206T133834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9a4ca030a901e12f4dcd5383def775d44b0175012a5d4f93e3e44b4c5bf0b492) = 9

## 14. My talents fall within definite limitations
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/6/44057bed4938503a9978.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221206T133834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=20f44f0b10751ef8f38bdf1459d036ebdc81d52958c692a183ba09c3720fb156) = ln(0) - ln(-1) is undefined

## 15. Winners are people with definite purpose in life
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/6/3d88d653f3ba869b43b1.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221206T133834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1e891547a34ea3f4e40a7b81edd199ac00577c43dfdb58e6527ecd30dd441ff9) = 5x

## 16. Double whammy
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/6/a2409c32448118661d05.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221206%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221206T133834Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d66bc26c9294eeee0dfffebf6daca79161619802e42ef82a76a4978e8414ca20) = 9ln(2)

## 17. Integrate
Write a function ``def poly_integral(poly, C=0):`` that calculates the integral of a polynomial:

`- poly is a list of coefficients representing a polynomial
    - the index of the list represents the power of x that the coefficient belongs to
    - Example: if f(x) = x^3 + 3x +5, poly is equal to [5, 3, 0, 1]
- C is an integer representing the integration constant
- If a coefficient is a whole number, it should be represented as an integer
- If poly or C are not valid, return None
- Return a new list of coefficients representing the integral of the polynomial
- The returned list should be as small as possible