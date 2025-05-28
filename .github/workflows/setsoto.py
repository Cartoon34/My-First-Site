<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Simple Landing Page</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background-color: #f7f9fc;
    }

    header {
      background-color: #4f46e5;
      color: white;
      padding: 40px 20px;
      text-align: center;
    }

    header h1 {
      margin: 0;
      font-size: 2.5rem;
    }

    header p {
      margin-top: 10px;
      font-size: 1.2rem;
      opacity: 0.9;
    }

    main {
      padding: 40px 20px;
      text-align: center;
    }

    .btn {
      display: inline-block;
      margin-top: 20px;
      padding: 12px 24px;
      font-size: 16px;
      background-color: #4f46e5;
      color: white;
      border: none;
      border-radius: 6px;
      text-decoration: none;
      transition: background-color 0.3s ease;
    }

    .btn:hover {
      background-color: #3730a3;
    }

    footer {
      text-align: center;
      padding: 20px;
      background-color: #e2e8f0;
      font-size: 14px;
      color: #555;
    }

    @media (max-width: 600px) {
      header h1 {
        font-size: 2rem;
      }

      main {
        padding: 20px;
      }
    }
  </style>
</head>
<body>

  <header>
    <h1>Welcome to My Website</h1>
    <p>Your journey into web development begins here</p>
  </header>

  <main>
    <p>This is a simple responsive landing page built using HTML and CSS.</p>
    <a class="btn" href="#">Get Started</a>
  </main>

  <footer>
    &copy; 2025 My Website. All rights reserved.
  </footer>

</body>
</html>