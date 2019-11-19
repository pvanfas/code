<!-- changing directory -->
<?php bloginfo('template_directory') ?>/

<!-- adding header and footer -->
<?php wp_head(); ?>
<?php get_header(); ?>
<?php wp_footer(); ?>
<?php get_footer(); ?>

<!-- Registering Menu (functions.php) -->
<?php 
	function register_menu() {
	  register_nav_menu('header-menu',__( 'Header Menu' ));
	}
	add_action( 'init', 'register_menu' );
?>

<!-- Defining navigation (replace in nav) -->
<?php 
	$args = array(
		"menu" => "Primary Menu",
		"container" => "ul"
	 );
	wp_nav_menu($args); 
?>

<!-- fixing logo url -->
<?php get_home_url(); ?>


<!-- add the following lines to functions.php-->

<?php 
// Registering Menu
function register_menu() {
  register_nav_menu('header-menu',__( 'Header Menu' ));
}
add_action( 'init', 'register_menu' );

// featured image support
add_theme_support('post-thumbnails');

// Custom post types
function create_posttype() {
    register_post_type('faculties',
        array(
            'labels' => array(
                'name' => __('Faculties'),
                'singular_name' => __('Faculty'), // Dash icons for custom post types
            ),
            'public' => true,
            'has_archive' => true,
            'menu_icon' => 'dashicons-groups', // https://developer.wordpress.org/resource/dashicons/
            'supports' => array('titile', 'editor', 'thumbnail')
        )
    );
    //add more here
}
add_action( 'init', 'create_posttype' );


?><!-- not required -->


<!-- adding custom elements to homepage -->
<!-- add the line to index page -->
<? php 
    $args = array(
        "post_type" => "page",
        "post_in" => array(99) //display page id
    );
    $about_page_query = new WP_Query($args);
    if($about_page_query->haveposts()){
        while($about_page_query->haveposts()){
        	$about_page_query->the_post();
        	$about_page_query->the_content();
        }
    }else{

    }
?>
 