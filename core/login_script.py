U
    ���]!  �                   @   s�   d dl Z d dlmZ d dlZdZdZdZdZdZdZd	Z	d
Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zedkr�e�  dS )�    N)�getpassz
.creed.txtz[1;91mz[1;92m�[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                   C   s   t j�t�rt�  nt�  d S )N)�os�path�isfile�cread�login�singup� r
   r
   �login.py�setup   s    r   c               	   C   s
  �zPt �  ttd � ttd � ttd � td� t�d� td� ttd � td� ttd��} td	�}td� ttd
 �}td� tt	d � td� td�}|dks�|�r,t
td��d}|�| � |�d� |�|� |�d� |�|� |��  td� tt	d � t�d� t�  W 5 Q R X n$td� ttd � t�d� t�  W n� tk
�r�   td� td� td� td� td� td� t�d� t�d� Y nZ tk
�r   td� td� td� td� td� td� t�d� t�d� Y nX d S )N� 	 Welcome to Termux �!---------------------------------� 	 CREATED BY HTR TECH � �date | lolcatr   �&SET USERNAME,PASSWORD AND RECOVERY KEYz[1;96mUsername [1;92m: z[1;96mPassword [1;92m: �Enter a Recovery key [1;92m: �H[+] Remember your recovery key.Without it you can't change username/pass�'[1;94mIf you agree hit Enter [1;94m: �w�
�DONE ! Initializing ...�      �?�     Wrong Input皙�����?z9[1;91m     UABLE TO SET THE USERNAME, PASSWORD, RECOVERY�333333�?�killall -9 com.termux)�clear�print�green�cyan�yellowr   �system�str�input�blue�openr   �write�close�time�sleep�exit�redr	   �	Exception�KeyboardInterrupt�ZusernameZpasswordZrecovery�x�fr
   r
   r   r	      sh    










r	   c               	   C   s  �zXt �  ttd � ttd � ttd � td� t�d� td� ttd � td� tttd ��} ttd	 �}td� ttd
 �}td� tt	d � td� td�}|dks�|�r4t
td��d}|�| � |�d� |�|� |�d� |�|� |��  td� tt	d � t�d� t�  W 5 Q R X n$td� ttd � t�d� t�  W n� tk
�r�   td� td� td� td� td� td� t�d� t�d� Y nZ tk
�r   td� td� td� td� td� td� t�d� t�d� Y nX d S )Nr   r   r   r   r   r   r   �Username [1;92m: zPassword [1;92m: r   r   r   r   r   r   r   r   r   z<[1;91m     UABLE TO CHANGE THE USERNAME, PASSWORD, RECOVERYr   )r   r   r    r!   r"   r   r#   r$   r%   r&   r'   r   r(   r)   r*   r+   r,   r-   �
singup_oner.   r/   r0   r
   r
   r   r4   N   sh    










r4   c               	   C   s*  t �  zxttd � ttd �} ttd��}|�� }|d �� }W 5 Q R X | |krZt	�  n"td� tt
d � t�d� W q W q  tk
r�   td� td� td� td� td� tt
d	 � t�d
� Y q  tk
�r"   td� td� td� td� td� tt
d � t�d
� Y q X q d S )Nz8[+] TO CHANGE THE PASSWORD PLEASE ENTER THE RECOVERY KEYz 
Enter your Recovery [1;92m: �r�   r   z    Invalid Recovery Keyr   r   z    Wrong Inputr   r   )r   r   r    r   r!   r'   r   �	readlines�rstripr4   r-   r*   r+   r.   r/   )ZrecZfi�dataZrecor
   r
   r   �change�   s:    
r:   c               	   C   s�  t �  ttd � ttd � ttd � td� t�d� td� ttd � td� ttd��.} | �	� }|d	 �
� }|d
 �
� }| ��  W 5 Q R X z�ttd �}td� ttd �}||kr�||kr�td� ttd |d� t�d� t �  W �q�n:|dk�s|dk�rt�  ntd� ttd � t�d� W q  tk
�r�   td� td� td� td� td� ttd � t�d� Y q  tk
�r�   td� td� td� td� td� ttd � t�d� Y q X q d S )Nz 	 Termux Login Script r   r   r   r   z<[+] To change password type "change" in username or passwordz[1;93m r5   r   �   r3   r   zPassword [1;92: z
 WELCOME ==> z[0mr   r:   r   r   )r   r   r    r!   r"   r   r#   r'   r   r7   r8   r)   r%   r   r*   r+   r:   r-   r.   r/   )Zflr9   �unameZpwordr   Zlogin2r
   r
   r   r   �   s\    

r   c                   C   s   t �d� d S )Nr   �r   r#   r
   r
   r
   r   r   �   s    r   c                   C   s   t �d� d S )Nr   r=   r
   r
   r
   r   r,   �   s    r,   �__main__)r   r   r*   r   r-   r    r"   r&   Zpurpler!   Zwhiter   r	   r4   r:   r   r   r,   �__name__r
   r
   r
   r   �<module>   s&   88"4