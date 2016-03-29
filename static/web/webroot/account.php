<?php
include(__DIR__.'/config.php');

    isset($res) ? $res = $res : $res = "nothing";

    $redis = new Predis\Client(array(
        "scheme" => "tcp",
        "host" => "127.0.0.1",
        "port" => 6379,
        "password" => "",
        "database" => 10,
        "persistent" => "0"));

    // Initial database set-up
    !$redis->exists('usercount') ? $redis->set("usercount", 0) : $res .= " (usercount: " . $redis->get("usercount") . ").";

    

if(isset($_POST['signup'])) {

    $username = $_POST['username'];
    $fullname = $_POST['username'];
    $email = $_POST['username'];
    $password = $_POST['password'];
    $profile = $_POST['username'];

    $newUserID = $redis->get("usercount");
    $key_user = "userID:" . $newUserID; // Note the semi-colon.

    // Hash and salt the new password.
    // \Sodium\sodium_init(); // Not in PHP libsodium
    // \Sodium\sodium_mlock($password); // Not in PHP libsodium
    $hash_str = \Sodium\crypto_pwhash_scryptsalsa208sha256_str(
        $password,
        \Sodium\CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_INTERACTIVE,
        \Sodium\CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_INTERACTIVE
    );
    // \Sodium\sodium_munlock($password); // Not in PHP libsodium


    // Step 1: Check if username is taken
//    Note: If the search parameter is a string and the type parameter is set to TRUE, the search is case-sensitive. in_array(search,array,type)
    if(in_array($username, $redis->hKeys('userlist'))) {
        echo "USERNAME EXISTS.";

    } else {

        // Step 2: Register the new username and corresponding ID in userlist.
        $res = $redis->hmset("userlist", [
            $username => $newUserID,
        ]);

        // Step 3: Create the new hash for the user.
        $res = $redis->hmset($key_user, [
            'username' => $username,
            'fullName' => $fullname,
            'email' => $email,
            'password' => $hash_str,
            'profile' => $profile,
        ]);

        // Step 4: Increment the usercount.
        $redis->incr("usercount");
    }


} else if(isset($_POST['login'])) {

    $username = $_POST['username'];
    $password = $_POST['password'];

    $key_user = "userID:" . $redis->hget("userlist", $username);
    $hash_str = $redis->hget($key_user, 'password');


    if (\Sodium\crypto_pwhash_scryptsalsa208sha256_str_verify($hash_str, $password)) {
        // recommended: wipe the plaintext password from memory
        \Sodium\memzero($password);

        $res .= "LOGGED IN.";
        // Password was valid
    } else {
        // recommended: wipe the plaintext password from memory
        \Sodium\memzero($password);
        
        $res .= "FAILED LOG IN.";
        // Password was invalid.
    }

} else if (isset($_GET['viewAccounts'])) {
    echo "Stored keys in redis:: ";
    Dump($redis->keys("*"));
    Dump($redis->hgetall("userlist"));
    // Dump($redis->hgetall("userID:0"));
}


$roo['title'] = "Sign-up";

$roo['header'] .= '<span class="siteslogan">Sign up for Ravensgrib</span>';
$roo['headerNvp'] .= '<p class="sitesloganNvp">Sign-Up</p>';

$roo['main'] = <<<EOD

<div class="articleSegment">
<h2>RavensGRIB sign up dev.</h2>
REDIT: $res
<form method="POST" action="account.php">
    <h3>Sign up form</h3>
    <div>
        Username
        <input type="text" placeholder="" value="" required="" name="username" />
    </div>
    <div>
        Full name
        <input type="text" placeholder="" value="" required="" name="fullname" />
    </div>
    <div>
        Profile
        <input type="text" placeholder="" value="" required="" name="profile" />
    </div>
    <div>
        Password
        <input type="text" placeholder="" value="" required="" name="password" />
    </div>
    <div>
        <input type="submit" value="Sign up" name="signup" /><br>
        <input type="submit" value="Log in" name="login" /><br>
        <input type="reset" value="Reset"><br>
        <a href="account.php?viewAccounts">Need help?</a><br>
    </div>
</form>

</div>

EOD;

$roo['footer'];

include(ROO_THEME_PATH);







