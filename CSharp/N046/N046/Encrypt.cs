using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace StringEncrypt
{
    public class Encrypt
    {
        #region 加密方法
        internal string ToEncrypt(string encryptKey, string str)
        {
            try
            {
                byte[] P_byte_key = //将密钥字符串转换为字节序列
                    Encoding.Unicode.GetBytes(encryptKey);
                byte[] P_byte_data = //将字符串转换为字节序列
                    Encoding.Unicode.GetBytes(str);
                MemoryStream P_Stream_MS = //创建内存流对象
                    new MemoryStream();
                CryptoStream P_CryptStream_Stream = //创建加密流对象
                    new CryptoStream(P_Stream_MS,new DESCryptoServiceProvider().
                   CreateEncryptor(P_byte_key, P_byte_key),CryptoStreamMode.Write);
                P_CryptStream_Stream.Write(//向加密流中写入字节序列
                    P_byte_data, 0, P_byte_data.Length);
                P_CryptStream_Stream.FlushFinalBlock();//将数据压入基础流
                byte[] P_bt_temp =//从内存流中获取字节序列
                    P_Stream_MS.ToArray();
                P_CryptStream_Stream.Close();//关闭加密流
                P_Stream_MS.Close();//关闭内存流
                return //方法返回加密后的字符串
                    Convert.ToBase64String(P_bt_temp);
            }
            catch (CryptographicException ce)
            {
                throw new Exception(ce.Message);
            }
        }

        internal string ToEncryptCopy(string encryptKey, string str)
        {
            try
            {
                byte[] p_byte_key = Encoding.Unicode.GetBytes(encryptKey);
                byte[] p_byte_str = Encoding.Unicode.GetBytes(str);

                MemoryStream memoryStream = new MemoryStream();//创建内存流对象
                CryptoStream cryptoStream = new CryptoStream(memoryStream,
                    new DESCryptoServiceProvider().CreateEncryptor(p_byte_key,p_byte_key),CryptoStreamMode.Write);

                cryptoStream.Write(p_byte_str, 0, p_byte_str.Length);
                cryptoStream.FlushFinalBlock();//将数据压入基础流
                byte[] p_bt_temp = memoryStream.ToArray();//从内存流中获取字节序列
                cryptoStream.Close();
                memoryStream.Close();

                return 
                    Convert.ToBase64String(p_bt_temp);
            }
            catch (CryptographicException ce)
            {
                throw new Exception(ce.Message);
            }
        }
        #endregion

        #region 解密方法
        internal string ToDecrypt(string encryptKey, string str)
        {
            try
            {
                byte[] P_byte_key = //将密钥字符串转换为字节序列
                    Encoding.Unicode.GetBytes(encryptKey);
                byte[] P_byte_data = //将加密后的字符串转换为字节序列
                    Convert.FromBase64String(str);
                MemoryStream P_Stream_MS =//创建内存流对象并写入数据
                    new MemoryStream(P_byte_data);
                CryptoStream P_CryptStream_Stream = //创建加密流对象
                    new CryptoStream(P_Stream_MS,new DESCryptoServiceProvider().
                    CreateDecryptor(P_byte_key, P_byte_key),CryptoStreamMode.Read);
                byte[] P_bt_temp = new byte[200];//创建字节序列对象
                MemoryStream P_MemoryStream_temp =//创建内存流对象
                    new MemoryStream();
                int i = 0;//创建记数器
                while ((i = P_CryptStream_Stream.Read(//使用while循环得到解密数据
                    P_bt_temp, 0, P_bt_temp.Length)) > 0)
                {
                    P_MemoryStream_temp.Write(//将解密后的数据放入内存流
                        P_bt_temp, 0, i);
                }
                return //方法返回解密后的字符串
                    Encoding.Unicode.GetString(P_MemoryStream_temp.ToArray());
            }
            catch (CryptographicException ce)
            {
                throw new Exception(ce.Message);
            }
        }

        internal string ToDecryptCopy(string encryptKey, string str) 
        {
            try
            {
                byte[] p_byte_data = Convert.FromBase64String(str);//将加密后的字符串转换成字节序列
                byte[] p_byte_key = Encoding.Unicode.GetBytes(encryptKey);

                MemoryStream p_memoryStream = new MemoryStream(p_byte_data);
                CryptoStream p_cryptoStream = new CryptoStream(p_memoryStream,
                    new DESCryptoServiceProvider().CreateDecryptor(p_byte_key, p_byte_key), CryptoStreamMode.Read);

                byte[] p_bt_temp = new byte[500];
                MemoryStream p_memroryStream_temp = new MemoryStream();
                int i = 0;
                while ((i = p_cryptoStream.Read(p_bt_temp,0,p_bt_temp.Length)) > 0)
                {
                    p_memroryStream_temp.Write(p_bt_temp,0,i);
                }

                return Encoding.Unicode.GetString(p_memroryStream_temp.ToArray());
            }
            catch (Exception)
            {

                throw;
            }
        }
        #endregion
    }
}
