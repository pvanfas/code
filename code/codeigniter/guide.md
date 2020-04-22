1. Install composer & Update php & xampp
```
sudo apt install wget php-cli php-zip unzip
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
HASH="$(wget -q -O - https://composer.github.io/installer.sig)"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
composer
```
```
sudo apt-add-repository ppa:ondrej/php
sudo apt-get install 7.3
sudo apt install php7.3-xdebug php7.3-curl php7.3-gd php7.3-xml php7.3-xmlrpc php7.3-mysql php7.3-mbstring php7.3-soap php 7.3-intl


```
```
sudo apt-get install mysql-server
mysql_secure_installation
systemctl status mysql.service
mysqladmin -p -u root version
sudo service mysql stop
run sudo /opt/lampp/xampp start
```
```
wget https://www.apachefriends.org/xampp-files/5.6.20/xampp-linux-x64-5.6.20-0-installer.run
sudo chmod +x xampp-linux-x64-5.6.20-0-installer.run
sudo ./xampp-linux-x64-5.6.20-0-installer.run
sudo /opt/lampp/xampp start
```

2. Initiate codeigniter
```
composer create-project CodeIgniter/framework project-name

composer create-project codeigniter4/appstarter project-name
```
3. Inital Setup
```
cd project-name
rm -rf readme.rst  user_guide contributing.md  license.txt

```

Set Base URL (application/config/config.php)

```
$config['base_url'] = 'http://localhost:3000';
```
Setup Database Credential (application/database.php)
```
$db['default'] = array(
    'dsn'   => '',
    'hostname' => 'localhost',
    'username' => 'root',
    'password' => '',
    'database' => 'project',
    'dbdriver' => 'mysqli',
    'dbprefix' => '',
    'pconnect' => FALSE,
    'db_debug' => (ENVIRONMENT !== 'production'),
    'cache_on' => FALSE,
    'cachedir' => '',
    'char_set' => 'utf8',
    'dbcollat' => 'utf8_general_ci',
    'swap_pre' => '',
    'encrypt' => FALSE,
    'compress' => FALSE,
    'stricton' => FALSE,
    'failover' => array(),
    'save_queries' => TRUE
);

```
Remove index.php (application/config/config.php)
```
//  Find the below code
    $config['index_page'] = "index.php"
//  Remove index.php
    $config['index_page'] = ""
```
Create .htaccess File
```
touch .htaccess
```
```
 RewriteEngine on
 RewriteCond $1 !^(index.php|resources|robots.txt)
 RewriteCond %{REQUEST_FILENAME} !-f
 RewriteCond %{REQUEST_FILENAME} !-d
 RewriteRule ^(.*)$ index.php/$1 [L,QSA]
```
Run project
```
php -S localhost:3000
```
3. Create database
4. Create Controller (application/controllers/Note.php)
```
<?php
class Note extends CI_Controller {
  
    public function __construct()
    {
        parent::__construct();
        $this->load->model('notes_model');
        $this->load->helper('url_helper');
        $this->load->helper('form');
        $this->load->library('form_validation');
    }
  
    public function index()
    {
        $data['notes'] = $this->notes_model->notes_list();
        $data['title'] = 'Notes List';
 
        $this->load->view('notes/list', $data);
    }
  
    public function create()
    {
        $data['title'] = 'Create Note';
        $this->load->view('notes/create', $data);
    }
      
    public function edit($id)
    {
        $id = $this->uri->segment(3);
        $data = array();
 
        if (empty($id))
        { 
         show_404();
        }else{
          $data['note'] = $this->notes_model->get_notes_by_id($id);
          $this->load->view('notes/edit', $data);
        }
    }
    public function store()
    {
 
        $this->form_validation->set_rules('title', 'Title', 'required');
        $this->form_validation->set_rules('description', 'Description', 'required');
 
        $id = $this->input->post('id');
 
        if ($this->form_validation->run() === FALSE)
        {  
            if(empty($id)){
              redirect( base_url('note/create') ); 
            }else{
             redirect( base_url('note/edit/'.$id) ); 
            }
        }
        else
        {
            $data['note'] = $this->notes_model->createOrUpdate();
            redirect( base_url('note') ); 
        }
         
    }
     
     
    public function delete()
    {
        $id = $this->uri->segment(3);
         
        if (empty($id))
        {
            show_404();
        }
                 
        $notes = $this->notes_model->delete($id);
         
        redirect( base_url('note') );        
    }
}

```
5. Make Model (application/models/Note_model.php)
```
<?php
class Notes_model extends CI_Model {
  
    public function __construct()
    {
        $this->load->database();
    }
     
    public function notes_list()
    {
        $query = $this->db->get('notes');
        return $query->result();
    }
     
    public function get_notes_by_id($id)
    {
        $query = $this->db->get_where('notes', array('id' => $id));
        return $query->row();
    }
     
    public function createOrUpdate()
    {
        $this->load->helper('url');
        $id = $this->input->post('id');
 
        $data = array(
            'title' => $this->input->post('title'),
            'description' => $this->input->post('description')
        );
        if (empty($id)) {
            return $this->db->insert('notes', $data);
        } else {
            $this->db->where('id', $id);
            return $this->db->update('notes', $data);
        }
    }
     
    public function delete($id)
    {
        $this->db->where('id', $id);
        return $this->db->delete('notes');
    }
}
```
6. Create Views
```
application/views/notes/create.php
application/views/notes/edit.php
application/views/notes/list.php
```
create.php
```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Codeigniter CRUD Application With Example - Tutsmake.com</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/css/bootstrap.css" rel="stylesheet">
    <style>
        .mt40{
            margin-top: 40px;
        }
    </style>
</head>
<body>
    
<div class="container">
  
<div class="row">
    <div class="col-lg-12 mt40">
        <div class="pull-left">
            <h2>Add Note</h2>
        </div>
    </div>
</div>
     
     
<form action="<?php echo base_url('note/store') ?>" method="POST" name="edit_note">
   <input type="hidden" name="id">
     <div class="row">
        <div class="col-md-12">
            <div class="form-group">
                <strong>Title</strong>
                <input type="text" name="title" class="form-control" placeholder="Enter Title">
            </div>
        </div>
        <div class="col-md-12">
            <div class="form-group">
                <strong>Description</strong>
                <textarea class="form-control" col="4" name="description"
                 placeholder="Enter Description"></textarea>
            </div>
        </div>
        <div class="col-md-12">
                <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>
     
 
</div>
     
</body>
</html>

```
edit.php
```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Codeigniter CRUD Application With Example - Tutsmake.com</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/css/bootstrap.css" rel="stylesheet">
    <style>
        .mt40{
            margin-top: 40px;
        }
    </style>
</head>
<body>
    
<div class="container">
  
<div class="row">
    <div class="col-lg-12 mt40">
        <div class="pull-left">
            <h2>Edit Note</h2>
        </div>
    </div>
</div>
     
     
<form action="<?php echo base_url('note/store') ?>" method="POST" name="edit_note">
   <input type="hidden" name="id" value="<?php echo $note->id ?>">
     <div class="row">
        <div class="col-md-12">
            <div class="form-group">
                <strong>Title</strong>
                <input type="text" name="title" class="form-control" value="<?php echo $note->title ?>" placeholder="Enter Title">
            </div>
        </div>
        <div class="col-md-12">
            <div class="form-group">
                <strong>Description</strong>
                <textarea class="form-control" col="4" name="description"
                 placeholder="Enter Description"><?php echo $note->description ?></textarea>
            </div>
        </div>
        <div class="col-md-12">
                <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>
     
 
</div>
     
</body>
</html>
```
list.php
```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Codeigniter CRUD Application With Example - Tutsmake.com</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha/css/bootstrap.css" rel="stylesheet">
    <style>
        .mt40{
            margin-top: 40px;
        }
    </style>
</head>
<body>
    
<div class="container">
    <div class="row mt40">
   <div class="col-md-10">
    <h2>Codeigniter Basic Crud Example - Tuts Make</h2>
   </div>
   <div class="col-md-2">
    <a href="<?php echo base_url('note/create/') ?>" class="btn btn-danger">Add Note</a>
   </div>
   <br><br>
 
    <table class="table table-bordered">
       <thead>
          <tr>
             <th>Id</th>
             <th>Title</th>
             <th>Description</th>
             <th>Created at</th>
             <td colspan="2">Action</td>
          </tr>
       </thead>
       <tbody>
          <?php if($notes): ?>
          <?php foreach($notes as $note): ?>
          <tr>
             <td><?php echo $note->id; ?></td>
             <td><?php echo $note->title; ?></td>
             <td><?php echo $note->description; ?></td>
             <td><a href="<?php echo base_url('note/edit/'.$note->id) ?>" class="btn btn-primary">Edit</a></td>
                 <td>
                <form action="<?php echo base_url('note/delete/'.$note->id) ?>" method="post">
                  <button class="btn btn-danger" type="submit">Delete</button>
                </form>
            </td>
          </tr>
         <?php endforeach; ?>
         <?php endif; ?>
       </tbody>
    </table>
    
</div>
 
</div>
     
</body>
</html>
```



