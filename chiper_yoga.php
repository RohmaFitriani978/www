<?php
$text = "fasilkom";
$key = 3;
$out = "";

for ($i=0; $i<strlen($text); $i++) {
    $c = $text[$i];
    $out .= chr((ord($c)-97+$key)%26+97);
}

echo $out; 