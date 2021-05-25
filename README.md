# matrix-encrypt

[中文](#matrix-encrypt中文版介绍) English

A few months ago I thought of several matrix encryption algorithms, and several encryption algorithms that have nothing to do with matrices, and all of them were implemented in python, a total of 9 encryption algorithms, and now I have made an exe file to put all 9 algorithms, including the encryption and decryption procedures. These 9 kinds of algorithms are my own free time to come up with, I guess several algorithms in the past should have been thought of and have been implemented, but this is even coincidental.

The matrix library matrix.py used in this project is also a python library developed by myself, which has very rich mathematical statistics and analysis functions about matrices, I will find time to make this library public as a project and introduce it to you later.

Most of the 9 encryption algorithms I have thought of are applicable to any file on the computer, i.e. there is no limit to the type of file. I will introduce them one by one.

The 1st encryption algorithm:

Encryption: Take the downward rounded square root of the total number of characters of the file to be encrypted as the dimension (number of rows and columns) to generate a square matrix, where each element of the square matrix is a random number picked from the range between two integers. You need to make sure that the determinant of this random number matrix is not zero, i.e., it is guaranteed to be invertible. All the characters of the file to be encrypted are converted to ASCII and then loaded into a square matrix of the same size, then the ASCII matrix of the encrypted file is multiplied by the random number matrix, and the new matrix is translated from ASCII back to characters, and then all the elements of the new matrix are taken out as ciphertext. The random number matrix needs to be saved as a key as well.

Decryption: The ASCII matrix of the ciphertext is multiplied by the inverse of the key matrix to get the ASCII matrix of the plaintext, which is then converted from ASCII to characters to decrypt it into plaintext.

Evaluation: This 1st algorithm needs to calculate the inverse of the matrix when decrypting, so the amount of operations is very large in the case of relatively large files, and the efficiency will be problematic, so this algorithm is more suitable for encrypting small files, especially for encrypting text files, such as encrypting an article, encrypting links, encrypting some text information, and so on. But the biggest advantage of this algorithm is that the degree of encryption is very high, because each element of the encryption matrix is a random number, and the value of each element will have an impact on the content of the ciphertext (because it is the product of the encryption matrix and the ASCII matrix of the plaintext), so there is no possibility of exhaustive running dictionary brute force cracking, because this is much more than the possibility of a simple one-line password. The disadvantage is that for larger files, the encryption and decryption time takes a long time, so it is suitable for smaller files (about 1MB or less)

The 2nd encryption algorithm:

Encryption: Shift each 8bit integer of the plaintext bytes array by a random number in positive or negative direction first, and then divide by a random integer (chosen from the range between two integers), the divisor is converted from ASCII to characters as ciphertext, and the remainder of the array and the array of random integers is used as the key, which is faster and suitable for encrypting larger files.

Decryption: Multiply each 8bit integer of the ciphertext bytes array by the corresponding divisor, add the corresponding remainder, and then shift back to the random number at the time of encryption to get the bytes array of the original text, and write it to the new file in binary form to decrypt it to the original file.

Evaluation: Compared with the 1st encryption algorithm, this algorithm has nothing to do with matrix, so there is no need to calculate the inverse of the matrix or the product of the matrix, only to shift each byte and divide it with a random integer. The divisor and remainder are taken as the ciphertext and key respectively, which is much faster than the 1st algorithm, so it is very suitable for encrypting larger files. The disadvantage is that the encryption level is obviously not as high as the matrix encryption of the 1st encryption algorithm, but in fact, the array of remainders as the key file is also much higher than the encryption level of a one-line cipher.

The 3rd encryption algorithm:

Encryption: Read the file in binary form, get the array of its bytes, reverse the order of the array, form the ciphertext, and form the encrypted file in binary form. The speed is the fastest among several algorithms, and it is more suitable for encrypting large files.

Decryption: Read the file in binary form, get the array of bytes, reverse the order of the array, and decrypt it to the original file.

Evaluation: This is a very simple and hardcore encryption algorithm, which does not need any key or any settings, but simply takes the binary bytes array of a file in reverse order as the cipher text, so the speed of encryption and decryption is also huge, so it can be used to encrypt very large files (after my actual test, the speed is also very good when encrypting and decrypting large files), this algorithm This algorithm seems to be very simple, but in fact it is very useful in some emergency situations, and the key is that when others do not know what algorithm you are using to encrypt the file, it is impossible to decrypt the original file anyway, after all, this algorithm does not have a key. In addition, it is obvious that this encryption algorithm is not very suitable for encrypting plain text files, because after encryption, the content of the text is just reversed, which feels like not much encrypted 23333, so this algorithm is suitable for encrypting any type of files other than plain text files.

The 4th type of encryption algorithm:

Encryption: Take the square root of the bytes array of the file to be encrypted as the downward integer to generate a random permutation matrix, multiply the permutation matrix left by the matrix of the bytes array of the file to be encrypted, and then get the new matrix of the bytes array of the file to be encrypted after a random horizontal exchange, and then get the cipher text, the key is the random permutation matrix.

Decryption: Read the file in binary form, get the array of bytes, multiply the inverse of the key matrix by the matrix of the array of bytes to decrypt the original file.

Evaluation: This algorithm is a faster version of the 1st algorithm, because the matrix used here is a permutation matrix, and one of the characteristics of a permutation matrix is that its inverse is equal to its transpose, so actually when decrypting we do not need to calculate the inverse of the key matrix, but only the transpose of the key matrix can be used to decrypt. It is much faster to compute the transpose of a large matrix than to compute the inverse of a large matrix. This algorithm is therefore more suitable for encrypting larger files.

The 5th encryption algorithm:

The advantage of using a diagonal matrix is that when decrypting the key matrix, only the transpose of the matrix needs to be calculated (because one of the properties of an orthogonal matrix is that its inverse is equal to its transpose), thus greatly speeding up the decryption process (the arithmetic power required to calculate the inverse of a large matrix is often much larger than the computation of its transpose) is more suitable for encryption and decryption of large files. Another difference from the 1st encryption algorithm is that the encryption object here is an array of bytes of the file.

Decryption: Calculate the inverse of the key matrix (the diagonal matrix belongs to the orthogonal matrix, and its inverse is equal to its transpose), then multiply the matrix of the bytes array of the encrypted file by the inverse of the key matrix to decrypt the original file.

Evaluation: The 5th algorithm is also similar to the 4th algorithm, which is also a fast version of the 1st algorithm. The difference between here and the 4th algorithm is that the diagonal matrix is used to encrypt.

The 6th encryption algorithm:

Encryption: Read the file in binary form, get its array of bytes, load the array into a square matrix with the dimension of the number of bytes of the file taking the square root of the downward integer, transpose the matrix, take out all the elements as the array of bytes of the ciphertext, and write it to a new file to get the encrypted file.

Decryption: Read the file in binary form, get its array of bytes, load the array into a square matrix whose dimension is the number of bytes of the file, transpose the matrix, take out all the elements as the new array of bytes, and then subtract the number of bits overflowed from the previous matrix to decrypt the original file.

Evaluation: This is a very fast encryption and decryption algorithm, also very suitable for encrypting larger files, and the encryption degree is good, but it is not suitable for encrypting plain text files, because after encryption is plain text as a transpose of the matrix, still the original content can be seen, so this algorithm is suitable for encrypting all types of files except plain text files.

The 7th encryption algorithm:

Encryption: change the byte at a random position in the bytes array of the file to a random byte integer (0-255), and execute the specified number of times to get the encrypted file. The key is the set of meta ancestors of the changed location and the value before the change.

Decryption: Decrypt the file by changing the bytes stored in the key back to the original value of the previously changed bytes.

Evaluation: This is an encryption algorithm that selectively and destructively encrypts the contents of plaintext, the degree of encryption depends on the set number of times to change bytes, the speed of encryption and decryption is relatively fast, and it is also very suitable for encrypting large files.

The 8th encryption algorithm:

Encryption: Read the file in binary form, get its array of bytes, line up the odd bits of the array together to form an odd bytes array and the even bits together to form an even bytes array, then connect the odd bytes array to the even bytes array to get the ciphertext.

Decryption: Read the file in binary form, get its array of bytes, divide the array into two halves according to the length, form two new bytes arrays, take out one of each of the two bytes arrays at a time, until both bytes arrays are traversed, then decrypt the file to the original.

Evaluation: This algorithm is to reorder the binary bytes array of a file by the rules of arranging the elements of the array, and the decryption is to apply the reverse rule of this rule to the ciphertext to get the plaintext. The encryption level I think is still very high, and no key is needed, and the speed of encryption and decryption is also very fast, which is very suitable for encrypting large files. In addition, this algorithm is also good for encrypting plain text files, and the original content is almost invisible after encryption.

The 9th encryption algorithm:

Encryption: Read the file to be encrypted in binary form and get an array of its bytes. The set password is converted into a list of ASCII codes, and then each byte is shifted in a positive direction from the first to the last cycle. The array of bytes after shifting is converted into characters according to ASCII code to form a cipher text in the format of a text file.

Decryption: The entered cipher is converted into ASCII code and the ASCII code corresponding to the characters of the cipher text is shifted in the negative direction from the first to the last cycle to decrypt the original file.

Evaluation: This algorithm uses a string of passwords set by the encryptor to encrypt, and shifts the current byte of the plaintext with the ASCII code corresponding to each bit of the password (the password is encrypted cyclically from the beginning to the end, that is, the first bit of the password is shifted to the current byte of the plaintext, the second bit of the password is shifted to the next byte of the plaintext, and when the last bit of the password is used up, it returns to the first bit of the password to continue). (The range of a byte is 0~255, so after shifting the bytes array with the set password, there is a possibility that the bytes after shifting exceeds 255, and then it is impossible to write the file in binary form. Therefore, this algorithm converts each element of the shifted bytes array into ASCII characters to form a ciphertext file in the format of a text file, so as to avoid the byte value overflow. The speed of encryption and decryption of this algorithm is very fast, which is very suitable for encrypting large files, and at the same time, as long as the more complex password you set, the higher the degree of damage to the file to be encrypted, the higher the degree of encryption will be, which will also make the decryption more difficult.

I have used python code to implement all the 9 encryption algorithms I want, and have integrated them all into an exe file that can be used directly, so you can choose any one of them to encrypt or decrypt any file. The evaluation of each of the above algorithms is after I have implemented the algorithms in code, after many times of actual encryption and decryption of multiple files after the test. You can also experience what the evaluation says when you use these algorithms to encrypt and decrypt files yourself.

# matrix-encrypt中文版介绍

中文 [English](#matrix-encrypt)

几个月前我想了几种矩阵加密的算法，还有几种跟矩阵没什么关系的加密算法，并且全部用python实现了，一共9种加密算法，现在我已经做了一个exe文件，把这9种算法全部放进去了，包括加密和解密的程序。这9种算法都是我自己平时空闲的时候想出来的，我估计个别几种算法在以前应该是早有人想到过并且已经实现过了，不过这就算是巧合了。

这个项目里用到的矩阵库matrix.py也是我自己一个人开发出来的python库，里面有着非常丰富的关于矩阵的很全面的数学统计计算与分析的功能，在以后我会找时间把这个库公开为一个项目，给大家介绍一下。

我想的这9种加密算法中的绝大部分都是适用于电脑上的任何文件的，也就是不限文件的类型。接下来我一个一个介绍。

第1种加密算法：

加密：以要加密的文件的总字符数量的向下取整平方根作为维数（行数和列数）生成一个方块矩阵，方块矩阵里的每个元素都是从两个整数之间的范围里挑选的随机数。需要确保这个随机数矩阵的行列式不为0，也就是保证可逆。把要加密的文件的字符全部转换成ASCII码然后装入一个同样大小的方块矩阵，然后将加密文件的ASCII码矩阵乘以随机数矩阵，得到的新矩阵再从ASCII码翻译回字符，然后把新矩阵的所有元素取出来作为密文。随机数矩阵作为密钥也需要保存起来。

解密：以密文的ASCII码矩阵乘上密钥矩阵的逆即可得到明文的ASCII码矩阵，再从ASCII码转换成字符即可解密为明文。

评价：这个第1种算法由于解密时需要计算矩阵的逆，所以在比较大的文件的情况下运算量非常大，效率会有问题，因此这个算法比较适用于加密小型文件，尤其适用于加密文本文件，比如加密一篇文章，加密链接，加密一些文本信息等等。但是这种算法最大的优点就是加密的程度非常高，因为加密矩阵的每一个元素都是随机数，每一个元素的值都会对密文的内容产生影响（因为是加密矩阵和明文的ASCII码矩阵的乘积），因此不存在有穷举跑字典暴力破解的可能性，因为这个比单纯一行密码的可能性还要多太多了。缺点就是对于大一些的文件，加密解密的时间需要很久，因此适用于比较小的文件（大约1MB以下的文件）

第2种加密算法：

加密：把明文的bytes数组每个8bit整数先进行正或负方向的随机数的移位，然后除以一个随机的整数（从两个整数之间的范围里选择），除数从ASCII码转换成字符作为密文，余数的数组和随机整数的数组作为密钥，速度较快，适合加密比较大的文件。

解密：把密文的bytes数组每个8bit整数乘上对应的被除数，再加上对应的余数，然后再移位回加密时的随机数即可得到原文的bytes数组，以二进制形式写入新文件即可解密为原文件。

评价：与第1种加密算法相比，这种算法跟矩阵无关，因此不需要计算矩阵的逆，也不需要计算矩阵的乘积，只有对每个byte进行移位，然后与一个随机的整数相除。取除数和余数分别作为密文和密钥，速度比第1种算法要快很多，因此很适用于加密比较大的文件。缺点是加密程度很明显并没有第1种加密算法的矩阵加密高，但是实际上作为密钥文件的余数的数组同样也是比起一行密码的加密程度要高很多。

第3种加密算法：

加密：以二进制形式读取文件，得到其bytes的数组，将数组倒序，形成密文，以二进制的形式形成加密的文件。速度是几种算法里最快的，更加适用于加密大型文件。

解密：以二进制形式读取文件，得到其bytes的数组，将数组倒序，即可解密为原文件。

评价：这是一种非常简单硬核的加密算法，不需要任何密钥，也不需要任何设置，只是单纯地把一个文件的二进制的bytes数组倒序作为密文，因此加密和解密的速度也是巨快，因此可以用来加密很大型的文件（经过我的实测，在加密和解密大型文件的时候速度也是很不错的），这个算法看似很简单，但是实际上在一些紧急的情况非常派得上用场，而且关键是当别人不知道你这个文件是用什么算法加密的情况下，他就无论如何也不可能解密出原文件，毕竟这个算法没有密钥。另外，很明显这种加密算法不是很适用于加密纯文本文件，因为加密之后只是文本的内容全文颠倒，感觉就等于没怎么加密了23333，因此这种算法适用于加密除了纯文本文件以外的任何类型的文件。

第4种加密算法：

加密：以要加密的文件的bytes数组的向下取整平方根为维度生成一个随机的置换矩阵，将置换矩阵左乘以要加密的文件的bytes数组的矩阵，即可得到要加密的文件的bytes数组的矩阵的随机横行交换过后得到的新的数组，即可得到密文，密钥为随机的置换矩阵。

解密：以二进制形式读取文件，得到其bytes的数组，将密钥矩阵的逆乘以bytes的数组的矩阵即可解密为原文件。

评价：这个算法算是第1种算法的比较快的版本，因为这里用来加密的矩阵是置换矩阵，置换矩阵的一个特性就是它的逆等于它的转置，因此实际上在解密的时候我们不需要去计算密钥矩阵的逆，而只需要计算密钥矩阵的转置就可以用来解密了。计算一个大型矩阵的转置可比计算一个大型矩阵的逆要快太多了。这个算法也因此比较适用于加密比较大的文件。

第5种加密算法：

加密：使用正交矩阵来对文件进行加密，在这里为对角矩阵，加密的细节与第一种加密算法类似，使用对角矩阵加密的好处是解密的时候计算密钥矩阵的逆只需要计算矩阵的转置（因为正交矩阵的一个性质就是其逆等于其转置），从而大大加快了解密的速度，（计算一个大型矩阵的逆所费的算力往往要远大于计算其转置）更加适用于大型文件的加密和解密。另外一个与第一种加密算法的区别是这里的加密对象是文件的bytes数组。

解密：计算密钥矩阵的逆(对角矩阵属于正交矩阵，其逆等于其转置)，然后用加密的文件的bytes数组的矩阵乘以密钥矩阵的逆，即可解密为原文件。

评价：第5种算法也和第4种算法类似，也是第1种算法的快速版，这里和第4种算法的区别在于使用的是对角矩阵来加密。

第6种加密算法：

加密：以二进制形式读取文件，得到其bytes的数组，将数组装入一个维度为文件的bytes数量的向下取整平方根的方块矩阵，将矩阵进行转置，取出所有元素作为密文的bytes数组，写入新文件即可得到加密的文件。

解密：以二进制形式读取文件，得到其bytes的数组，将数组装入一个维度为文件的bytes数量的向下取整平方根的方块矩阵，将矩阵进行转置，取出所有元素作为新的bytes数组，再减去之前矩阵溢出的位数即可解密为原文件。

评价：这是一种加密和解密速度很快的算法，也很适用于加密比较大型的文件，加密程度也不错，不过不适用于加密纯文本文件，因为加密过后就是明文作为一个矩阵的转置，还是可以看出原文的内容，因此这种算法适用于加密除纯文本文件以外的所有类型的文件。

第7种加密算法：

加密：在文件的bytes数组的随机的位置上的byte改变成随机的byte整数(0-255)，执行指定的次数，即可得到加密后的文件。（每次选择的位置会保证跟之前的不重复）密钥为改变的位置和改变之前的值的元祖集合。

解密：将密钥里存储的之前改变bytes的位置的bytes改变回原值，即可解密为原文件。

评价：这是一种对明文的内容进行选择性的破坏性加密的加密算法，加密程度取决于设定的改变bytes的次数，加密和解密的速度比较快，也很适用于加密大型的文件。

第8种加密算法：

加密：以二进制形式读取文件，得到其bytes的数组，将数组的奇数位排在一起形成奇数bytes数列，偶数位排在一起形成偶数bytes数列，然后把奇数bytes数列接上偶数bytes数列，即可得到密文。

解密：以二进制形式读取文件，得到其bytes的数组，将数组按照长度分成两半，形成两个新的bytes数组，两个bytes数组每次各自拿出一个，直到两个bytes数组都遍历完，即可解密为原文件。

评价：这个算法是通过一个数组的元素排列规则对一个文件的二进制的bytes数组进行重新排序，解密的时候就是把这个规则的逆向规则应用到密文即可得到明文。加密程度我认为还是很高的，而且不需要密钥，加密和解密的速度也很快，很适用于加密大型的文件。此外，这个算法用来加密纯文本文件也不错，加密过后几乎看不出来原来的内容是什么。

第9种加密算法：

加密：以二进制形式读取要加密的文件，得到其bytes的数组。设定的密码转换成ASCII码的列表，然后从第一个到最后一个循环对每一个bytes进行正方向的移位。移位之后的bytes数组按照ASCII码转换成字符，以文本文件的格式形成密文。

解密：输入的密码转换成ASCII码对密文的字符对应的ASCII码进行从第一个到最后一个的循环的负方向的移位，即可解密为原文件。

评价：这个算法使用加密者设定的一串密码来进行加密，以密码每一位对应的ASCII码对明文的当前对应的byte进行移位（密码从头到尾循环加密，也就是从密码的第1位开始对明文的当前byte移位，密码的第2位对明文的下一位byte移位，等到密码的最后一位用完了再回到密码的第1位继续），由于一个byte的范围是0~255，因此在使用设定的密码对bytes数组进行移位之后，有可能出现移位后的bytes超过255的情况，此时就无法以二进制的形式写入密文的文件了，因此这个算法在加密之后将移位后的bytes数组里的每个元素按照ASCII码转换成字符，以文本文件的格式形成密文的文件，这样可以避免byte的值溢出的情况。这种算法的加密和解密的速度非常快，很适用于加密大型的文件，同时只要你设定的密码越复杂，对要加密的文件的破坏程度就越高，加密程度也就越高，也会让解密的难度更高。

这9种我想的加密算法我已经全部用python代码实现，并且已经把这9种加密算法全部集成到一个exe文件里可以直接使用，可以选择任何一种算法来加密或者解密任何的文件。以上每个算法的评价都是我在用代码实现了算法之后，经过多次实际的加密和解密多个文件的测试之后得出的。大家在自己使用这些加密算法对文件进行加密和解密的时候也能体会到评价所说的内容。

