<?php

include "db.inc.php";
include "validation.inc.php";
session_start();
$isLoggedIn = isset($_SESSION['isloggedin']) && $_SESSION['isloggedin'] == true;
if (isset($_SESSION['email'])) {
  $email = setup_input($_SESSION['email']);
  $result = fetchUser("email", $email, "user_table");
  if ($result->num_rows > 0){
    
    $row = $result->fetch_assoc();
    $user_id = $row['id'];
    $sql = "SELECT p.product_id, p.product_name, p.product_image_url, p.product_price, p.quantity
          FROM user_carted_product uc
          INNER JOIN product_table p ON uc.carted_product_id = p.product_id
          WHERE uc.user_id = $user_id";
    $result1 = $conn->query($sql);

    if ($result1 === false) {
      die("Query failed: " . $conn->error);
    }
    $sql1 = "SELECT p.product_id, p.product_name, p.product_price, p.product_image_url
    FROM product_table p
    INNER JOIN user_carted_product uc ON p.product_id = uc.carted_product_id
    WHERE uc.user_id = $user_id";
    ;
    $products = $conn->query($sql1);
    $sql4 = "SELECT * FROM checkout_products WHERE user_id = $user_id AND status = 'pending'";
    $result4 = $conn->query($sql4);
  }
}
?>
<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>EDF</title>
    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!-- Favicon -->
    <link rel="shortcut icon" type="image/x-icon" href="img/logo.png" />
    <!-- Google Fonts -->
    <link
      href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i"
      rel="stylesheet"
    />
    <!-- CSS
	============================================ -->
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css" />
    <!-- Icon Font CSS -->
    <link rel="stylesheet" href="css/font-awesome.min.css" />
    <link rel="stylesheet" href="css/ionicons.min.css" />
    <!-- Plugins CSS -->
    <link rel="stylesheet" href="css/plugins.css" />
    <!-- Style CSS -->
    <link rel="stylesheet" href="style.css" />
    <!-- Modernizer JS -->
    <script src="js/vendor/modernizr-2.8.3.min.js"></script>
  </head>

  <body>
    <!-- Main Wrapper Start -->
    <div id="main-wrapper" class="section">
      <!-- Header Section Start -->
      <div class="header-section section">
        <!-- Header Top Start -->
        <div class="header-top">
          <div class="container">
            <div class="row">
              <div class="col">
                <!-- Header Top Wrapper Start -->
                <div class="header-top-wrapper">
                  <div class="row">
                    <!-- Header Social -->
                    <div class="header-social col-md-4 col-12">
                        <a href="#"><i class="fa fa-telegram"></i></a>
                        <a href="#"><i class="fa fa-twitter"></i></a>
                        <a href="#"><i class="fa fa-linkedin"></i></a>
                        <a href="#"><i class="fa fa-instagram"></i></a>
                        <a href="#"><i class="fa fa-facebook"></i></a>
                      </div>
  

                    <!-- Header Logo -->
                    <div class="header-logo col-md-4 col-12">
                      <a href="index.php" class="logo"
                        ><img src="img/logo.png" alt="logo"
                      /></a>
                    </div>

                    <!-- Account Menu -->
                    <div class="account-menu col-md-4 col-12">
                    <?php
                    if($isLoggedIn){
                      $num = $result1->num_rows;
                    }
                      ?>
                      <ul>
                        <li><a href="index.php">My Account</a></li>
                        <li><a href="wishlist.php">Wishlist</a></li>
                        <li>
    <a href="#" data-toggle="dropdown">
        <i class="fa fa-shopping-cart"></i>
        <?php 
        if ($isLoggedIn) {
            echo '<span class="num">' . $num . '</span>';
        } else {
            echo '<span class="num">0</span>';
        }
        ?>
    </a>

    <!-- Mini Cart -->
    <div class="mini-cart-brief dropdown-menu text-left">
        <!-- Cart Products -->
        <div class="all-cart-product clearfix">
        <?php
        if ($isLoggedIn) {
            while ($row1 = $result1->fetch_assoc()) {
                $product_name = $row1['product_name'];
                $product_image_url = $row1['product_image_url'];
                $product_price = $row1['product_price'];
                $quantity = $row1['quantity'];

                // Generate a unique ID for the <span> tag
                $span_id = 'prodquantity_' . $row1['product_id'];
                ?>
                <div class="single-cart clearfix">
                    <div class="cart-image">
                        <a href="product-details.php"><img src="<?php echo $product_image_url; ?>" alt="" /></a>
                    </div>
                    <div class="cart-info">
                        <h5><a href="product-details.php"><?php echo $product_name; ?></a></h5>
                        <span id="<?php echo $span_id; ?>"><?php echo $quantity; ?></span> x <?php echo '$'.$product_price; ?></p>
                    </div>
                </div>
                <?php
            }
        } else {
            ?>
            <div class="single-cart clearfix">
                <div class="cart-image">
                    <a href="product-details.html"><img src="img/product/man.jpg" alt="" /></a>
                </div>
                <div class="cart-info">
                    <h5><a href="product-details.html">Mango</a></h5>
                    <p>1 x 90.00</p>
                    <a href="#" class="cart-delete" title="Remove this item"><i class="fa fa-trash-o"></i></a>
                </div>
            </div>
            <div class="single-cart clearfix">
                <div class="cart-image">
                    <a href="product-details.html"><img src="img/product/avo.jpg" alt="" /></a>
                </div>
                <div class="cart-info">
                    <h5><a href="product-details.html">Avocado</a></h5>
                    <p>1 x 39.00</p>
                    <a href="#" class="cart-delete" title="Remove this item"><i class="fa fa-trash-o"></i></a>
                </div>
            </div>
            <?php
        }
        ?>

        <!-- Cart Total -->
        <div class="cart-totals">
            <h5>Total <span id="aboveCartTotal"><?php echo ($isLoggedIn) ? '$0' : '120$'; ?></span></h5>
        </div>
        <!-- Cart Button -->
        <div class="cart-bottom clearfix">
            <a href="<?php echo ($isLoggedIn) ? 'cart.php' : 'checkout.html'; ?>">
                <?php echo ($isLoggedIn) ? 'Go to Cart Page' : 'Check out'; ?>
            </a>
        </div>
    </div>
</li>

<?php
if ($isLoggedIn) {
    echo '<li><a href="logoutlogic.php">Logout</a></li>';
} else {
    echo '<li><a href="animatedLogin.php">Login</a></li>';
}
?>
                  </div>
                </div>
                <!-- Header Top Wrapper End -->
              </div>
            </div>
          </div>
        </div>
        <!-- Header Top End -->

        <!-- Header Bottom Start -->
        <div class="header-bottom section">
          <div class="container">
            <div class="row">
              <!-- Header Bottom Wrapper Start -->
              <div class="header-bottom-wrapper text-center col">
                <!-- Header Bottom Logo -->
                <div class="header-bottom-logo">
                  <a href="index.php" class="logo"
                    ><img src="img/logo.png" alt="logo"
                  /></a>
                </div>

                <!-- Main Menu -->
                <nav id="main-menu" class="main-menu">
                  <ul>
                    <li><a href="index.php">home</a></li>
                    <li>
                      <a href="shop.php">shop</a>
                    </li>
                    <li><a href="about.php">about</a></li>
                    <li><a href="cart.php">cart</a></li>
                    <li class="active"><a href="checkout.php">checkout</a></li>
                    <li><a href="contact.php">contact</a></li>
                  </ul>
                </nav>

                <!-- Header Search -->
                <div class="header-search">
                  <!-- Search Toggle -->
                  <button class="search-toggle">
                    <i class="ion-ios-search-strong"></i>
                  </button>

                  <!-- Search Form -->
                  <div class="header-search-form">
                    <form action="#">
                      <input type="text" placeholder="Search..." />
                      <button><i class="ion-ios-search-strong"></i></button>
                    </form>
                  </div>
                </div>

                <!-- Mobile Menu -->
                <div class="mobile-menu section d-md-none"></div>
              </div>
              <!-- Header Bottom Wrapper End -->
            </div>
          </div>
        </div>
        <!-- Header Bottom End -->
      </div>
      <!-- Header Section End -->

      <!-- Page Banner Section Start-->
      <div
        class="page-banner-section section"
        style="background-image: url(img/bg/hjk.jpg)"
      >
        <div class="container">
          <div class="row">
            <!-- Page Title Start -->
            <div class="page-title text-center col">
              <h1>Checkout</h1>
            </div>
            <!-- Page Title End -->
          </div>
        </div>
      </div>
      <!-- Page Banner Section End-->

      <!-- Checkout Section Start-->
      <div class="cart-section section pt-120 pb-90">
        <div class="container">
          <div class="row">
            <div class="col-lg-6 col-12 mb-30">
              <!-- Checkout Accordion Start -->
              <div id="checkout-accordion" class="panel-group">
                <!-- Checkout Method -->
                <div class="panel single-accordion">
                  <a
                    class="accordion-head"
                    data-toggle="collapse"
                    data-parent="#checkout-accordion"
                    href="#checkout-method"
                    >1. checkout method</a
                  >

                  <div id="checkout-method" class="collapse show"   <?php if ($isLoggedIn) echo 'style="display: none;"'; ?>>
                    <div class="checkout-method accordion-body fix">
                      <ul class="checkout-method-list">
                        <li class="active" data-form="checkout-login-form">
                          Login
                        </li>
                        <li data-form="checkout-register-form">Register</li>
                      </ul>

                      <form action="login.php" class="checkout-login-form" method="POST">
                        <div class="row">
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="email" name="cemail" placeholder="Email Address" />
                          </div>
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="password" name="cpassword" placeholder="Password" />
                          </div>
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="submit" value="Login" />
                          </div>
                        </div>
                      </form>

                      <form action="#" class="checkout-register-form">
                        <div class="row">
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="text" placeholder="Your Name" />
                          </div>
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="email" placeholder="Email Address" />
                          </div>
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="password" placeholder="Password" />
                          </div>
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input
                              type="password"
                              placeholder="Confirm Password"
                            />
                          </div>
                          <div class="input-box col-md-6 col-12 mb-20">
                            <input type="submit" value="Register" />
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>

                <!-- Billing Method -->
                <div class="panel single-accordion">
                  <a
                    class="accordion-head collapsed"
                    data-toggle="collapse"
                    data-parent="#checkout-accordion"
                    href="#billing-method"
                    >2. billing informatioon</a
                  >
                  <div id="billing-method" class="collapse">
                    <div class="accordion-body billing-method fix">
                      <form action="#" class="billing-form checkout-form">
                        <div class="row">
                          <div class="col-12 mb-20">
                            <select>
                              <option value="1">Select a country</option>
                              <option value="2">bangladesh</option>
                              <option value="3">Algeria</option>
                              <option value="4">Afghanistan</option>
                              <option value="5">Ghana</option>
                              <option value="6">Albania</option>
                              <option value="7">Bahrain</option>
                              <option value="8">Colombia</option>
                              <option value="9">Dominican Republic</option>
                            </select>
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="text" placeholder="First Name" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="text" placeholder="Last Name" />
                          </div>
                          <div class="col-12 mb-20">
                            <input type="text" placeholder="Company Name" />
                          </div>
                          <div class="col-12 mb-20">
                            <input placeholder="Street address" type="text" />
                          </div>
                          <div class="col-12 mb-20">
                            <input
                              placeholder="Apartment, suite, unit etc. (optional)"
                              type="text"
                            />
                          </div>
                          <div class="col-12 mb-20">
                            <input placeholder="Town / City" type="text" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="text" placeholder="State / County" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input placeholder="Postcode / Zip" type="text" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="email" placeholder="Email Address" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input placeholder="Phone Number" type="text" />
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>

                <!-- Shipping Method -->
                <div class="panel single-accordion">
                  <a
                    class="accordion-head collapsed"
                    data-toggle="collapse"
                    data-parent="#checkout-accordion"
                    href="#shipping-method"
                    >3. shipping informatioon</a
                  >
                  <div id="shipping-method" class="collapse">
                    <div class="accordion-body shipping-method fix">
                      <h5>shipping address</h5>
                      <p>
                        <span>address&nbsp;</span>Bootexperts, Banasree D-Block,
                        Dhaka 1219, Bangladesh
                      </p>

                      <button class="shipping-form-toggle">
                        Ship to a different address?
                      </button>

                      <form action="#" class="shipping-form checkout-form">
                        <div class="row">
                          <div class="col-12 mb-20">
                            <select>
                              <option value="1">Select a country</option>
                              <option value="2">bangladesh</option>
                              <option value="3">Algeria</option>
                              <option value="4">Afghanistan</option>
                              <option value="5">Ghana</option>
                              <option value="6">Albania</option>
                              <option value="7">Bahrain</option>
                              <option value="8">Colombia</option>
                              <option value="9">Dominican Republic</option>
                            </select>
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="text" placeholder="First Name" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="text" placeholder="Last Name" />
                          </div>
                          <div class="col-12 mb-20">
                            <input type="text" placeholder="Company Name" />
                          </div>
                          <div class="col-12 mb-20">
                            <input placeholder="Street address" type="text" />
                          </div>
                          <div class="col-12 mb-20">
                            <input
                              placeholder="Apartment, suite, unit etc. (optional)"
                              type="text"
                            />
                          </div>
                          <div class="col-12 mb-20">
                            <input placeholder="Town / City" type="text" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="text" placeholder="State / County" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input placeholder="Postcode / Zip" type="text" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input type="email" placeholder="Email Address" />
                          </div>
                          <div class="col-md-6 col-12 mb-20">
                            <input placeholder="Phone Number" type="text" />
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>

                <!-- Payment Method -->
                <div class="panel single-accordion">
                  <a
                    class="accordion-head collapsed"
                    data-toggle="collapse"
                    data-parent="#checkout-accordion"
                    href="#payment-method"
                    >4. Payment method</a
                  >
                  <div id="payment-method" class="collapse">
                    <div class="accordion-body payment-method fix">
                      <ul class="payment-method-list">
                        <li class="active">check / money order</li>
                        <li class="payment-form-toggle">credit card</li>
                      </ul>

                      <form action="#" class="payment-form">
                        <div class="row">
                          <div class="input-box col-12 mb-20">
                            <label for="card-name">Name on Card *</label>
                            <input type="text" id="card-name" />
                          </div>
                          <div class="input-box col-12 mb-20">
                            <label>Credit Card Type</label>
                            <select>
                              <option>Please Select</option>
                              <option>Credit Card Type 1</option>
                              <option>Credit Card Type 2</option>
                            </select>
                          </div>
                          <div class="input-box col-12 mb-20">
                            <label for="card-number"
                              >Credit Card Number *</label
                            >
                            <input type="text" id="card-number" />
                          </div>
                          <div class="input-box col-12">
                            <div class="row">
                              <div class="input-box col-12">
                                <label>Expiration Date</label>
                              </div>
                              <div class="input-box col-md-6 col-12 mb-20">
                                <select>
                                  <option>Month</option>
                                  <option>Jan</option>
                                  <option>Feb</option>
                                  <option>Mar</option>
                                  <option>Apr</option>
                                  <option>May</option>
                                  <option>Jun</option>
                                  <option>Jul</option>
                                  <option>Aug</option>
                                  <option>Sep</option>
                                  <option>Oct</option>
                                  <option>Nov</option>
                                  <option>Dec</option>
                                </select>
                              </div>
                              <div class="input-box col-md-6 col-12 mb-20">
                                <select>
                                  <option>Year</option>
                                  <option>2015</option>
                                  <option>2016</option>
                                  <option>2017</option>
                                  <option>2018</option>
                                  <option>2019</option>
                                  <option>2020</option>
                                  <option>2021</option>
                                  <option>2022</option>
                                  <option>2023</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="input-box col-12">
                            <label for="card-Verify"
                              >Card Verification Number *</label
                            >
                            <input type="text" id="card-Verify" />
                            <a href="#">What is it ?</a>
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Checkout Accordion Start -->
            </div>

            <!-- Order Details -->
            <?php
if ($isLoggedIn) {
    echo '
    <div class="col-lg-6 col-12 mb-30">
        <div class="order-details-wrapper">
            <h2>your order</h2>
            <div class="order-details">
                <form action="#">
                    <ul>
                        <li>
                            <p class="strong">product</p>
                            <p class="strong">total</p>
                        </li>';
    
    $subtotal = 0;
    while ($row = mysqli_fetch_assoc($result4)) {
        $product = $row['product_name'];
        $quantity = $row['quantity'];
        $total = $row['total_price'];
        $subtotal += $total;
        
        echo '
        <li>
            <p>' . $product . ' x ' . $quantity . '</p>
            <p>$' . $total . '</p>
        </li>';
    }
    
    echo '
        <li>
            <p class="strong">cart subtotal</p>
            <p class="strong">$' . $subtotal . '</p>
        </li>
        <li>
            <p class="strong">shipping</p>
            <p>
                <input type="radio" name="order-shipping" id="flat" /><label for="flat">Flat Rate $ 7.00</label><br />
                <input type="radio" name="order-shipping" id="free" /><label for="free">Free Shipping</label>
            </p>
        </li>
        <li>
            <p class="strong">order total</p>
            <p class="strong">$' . $subtotal . '</p>
        </li>
        <li><button class="button">place order</button></li>
    </ul>
    </form>
    </div>
    </div>
    </div>';
} else {
    echo '<div class="checkwrapper">';
    echo '<p class="chechpara">No products in the cart</p>';
    echo '<div class="checkanch"><a href="shop.php">Go to Shop page</a></div>';
    echo '</div>';
}
?>


          </div>
        </div>
      </div>
      <!-- Checkout Section End-->

       <!-- Footer Section Start-->
       <div
       class="footer-section section bg-dark"
      
     >
       <div class="container">
         <div class="row">
           <div class="col">
             <!-- Footer Top Start -->
             <div class="footer-top section pt-80 pb-50">
               <div class="row">
                 <!-- Footer Widget -->
                 <div class="footer-widget col-lg-4 col-md-6 col-12 mb-40">
                   <img
                     class="footer-logo"
                     src="img/plol.png "
                     alt="logo"
                   />
                   
                 </div>

                 <!-- Footer Widget -->
                 <div class="footer-widget col-lg-2 col-md-3 col-12 mb-40">
                   <h4 class="widget-title">Information</h4>

                   <ul>
                     <li><a href="#">About us</a></li>
                     <li><a href="#">Shop</a></li>
                     <li><a href="#">Blog</a></li>
                     <li><a href="#">Portfolio</a></li>
                     <li><a href="#">Contact us</a></li>
                   </ul>
                 </div>

                 <!-- Footer Widget -->
                 <div class="footer-widget col-lg-2 col-md-3 col-12 mb-40">
                   <h4 class="widget-title">Categories</h4>

                   <ul>
                     <li><a href="#">Costumes</a></li>
                     <li><a href="#">Lights</a></li>
                     <li><a href="#">Lights</a></li>
                     <li><a href="#">Christmas Trees</a></li>
                     <li><a href="#">Decorations</a></li>
                   </ul>
                 </div>

                 <!-- Footer Widget -->
                 <div class="footer-widget col-lg-4 col-md-6 col-12 mb-40">
                   <h4 class="widget-title">Contact Us</h4>

                   <ul>
                     <li>
                       <span>Address:</span>Bole Sub City, Gollagul Tower,
                        
                   Addis Ababa

                     </li>
                     <li>
                       <span>Phone:</span> Tel: 011 667 30 04 , +251944106233
                     </li>
                 
           
                    
                     <li><span>Email:</span> contact@ethiopiandigitalfarmers.com</li>
                   </ul>
                 </div>
               </div>
             </div>
             <!-- Footer Top End -->

             <!-- Footer Bottom Start -->
             <div class="footer-bottom section text-center">
               <p><a href=>TouchBear</a></p>
             </div>
             <!-- Footer Bottom End -->
           </div>
         </div>
       </div>
     </div>
     <!-- Footer Section End-->
   </div>
   <!-- Main Wrapper End -->

   <!-- JS
============================================ -->

   <!-- jQuery JS -->
   <script src="js/vendor/jquery-1.12.0.min.js"></script>
   <!-- Popper JS -->
   <script src="js/popper.min.js"></script>
   <!-- Bootstrap JS -->
   <script src="js/bootstrap.min.js"></script>
   <!-- Plugins JS -->
   <script src="js/plugins.js"></script>
   <!-- Ajax Mail JS -->
   <script src="js/ajax-mail.js"></script>
   <!-- Main JS -->
   <script src="js/main.js"></script>
 </body>
</html>
