# Instagram-Bruteforcer
<h3>Instagram bruteforce coded in Python</h3>
<h3>for educational use and learning</h3>
<hr>

<h3>Installing on Arch</h3>
<pre>pacman -S python3 python-pip git --noconfirm</pre>
<pre>git clone https://github.com/joao406/Instagram-Bruteforce</pre>
<pre>cd InstaBrute</pre>
<pre>python3 bruteforce.py -u USERNAME -w WORDLIST</pre>

<h3>Installing on Debian/Ubuntu</h3>
<pre>apt install python3 python3-pip git</pre>
<pre>git clone https://github.com/joao406/Instagram-Bruteforce</pre>
<pre>cd InstaBrute</pre>
<pre>python3 bruteforce.py -u USERNAME -w WORDLIST</pre>

<hr>

<h3>Installing on Arch WITH TOR</h3>
<pre>pacman -S python3 python3-pip git proxychains-ng tor</pre>
<pre>git clone https://github.com/joao406/Instagram-Bruteforce</pre>
<pre>cd InstaBrute</pre>
<pre>sudo systemctl restart tor</pre>
<pre>proxychains -q python3 bruteforce.py -u USERNAME -w WORDLIST</pre>

<h3>Installing on Debian/Ubuntu WITH TOR</h3>
<pre>apt install python3 python3-pip git proxychains-ng tor -y</pre>
<pre>git clone https://github.com/joao406/Instagram-Bruteforce</pre>
<pre>cd InstaBrute</pre>
<pre>sudo systemctl restart tor</pre>
<pre>proxychains -q python3 bruteforce.py -u USERNAME -w WORDLIST</pre>
