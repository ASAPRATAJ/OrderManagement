import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const token = localStorage.getItem('token');
  const user = JSON.parse(localStorage.getItem('user')) || {};

  const isLoggedIn = !!token;
  const isStaff = user.isStaff || false;

  return (
    <nav
      className="p-4 shadow-md"
      style={{
        backgroundImage: "url('/images/lastryko.jpg')",
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo */}
        <div className="text-gray-800 text-2xl font-bold">
          <Link
            to="/"
            className="hover:text-gray-700 hover:shadow-md transition duration-300"
          >
            MyApp
          </Link>
        </div>

        {/* Links */}
        <ul className="flex space-x-6">
          <li>
            <Link
              to="/"
              className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
            >
              Home
            </Link>
          </li>

          {!isLoggedIn && (
            <>
              <li>
                <Link
                  to="/users/create"
                  className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                >
                  Create User
                </Link>
              </li>
              <li>
                <Link
                  to="/login"
                  className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                >
                  Login
                </Link>
              </li>
            </>
          )}

          {isLoggedIn && (
            <>
              <li>
                <Link
                  to="/orders/create"
                  className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                >
                  Create Order
                </Link>
              </li>
              <li>
                <Link
                  to="/products"
                  className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                >
                  Products
                </Link>
              </li>
              <li>
                <Link
                  to="/users/orders"
                  className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                >
                  Your Orders
                </Link>
              </li>

              {isStaff && (
                <>
                  <li>
                    <Link
                      to="/users"
                      className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                    >
                      Users
                    </Link>
                  </li>
                  <li>
                    <Link
                      to="/products/create"
                      className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                    >
                      Create Product
                    </Link>
                  </li>
                  <li>
                    <Link
                      to="/orders"
                      className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                    >
                      Orders
                    </Link>
                  </li>
                </>
              )}

              <li>
                <Link
                  to="/logout"
                  className="text-gray-800 font-bold hover:text-gray-700 hover:shadow-md transition duration-300"
                >
                  Logout
                </Link>
              </li>
            </>
          )}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
