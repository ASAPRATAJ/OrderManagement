import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
    const token = localStorage.getItem('token');
    const user = JSON.parse(localStorage.getItem('user')) || {};

    const isLoggedIn = !!token;
    const isStaff = user.isStaff || false;

    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">MyApp</Link>
            </div>
            <ul className="navbar-links">
                <li><Link to="/">Home</Link></li>

                {!isLoggedIn && (
                    <>
                        <li><Link to="/users/create">Create User</Link></li>
                        <li><Link to="/login">Login</Link></li>
                    </>
                )}

                {isLoggedIn && (
                    <>
                        <li><Link to="/orders/create">Create Order</Link></li>
                        <li><Link to="/users/orders">Your Orders</Link></li> {/* Dodano link do zamówień użytkownika */}

                        {isStaff && (
                            <>
                                <li><Link to="/users">Users</Link></li>
                                <li><Link to="/products">Products</Link></li>
                                <li><Link to="/products/create">Create Product</Link></li>
                                <li><Link to="/orders">Orders</Link></li>
                            </>
                        )}

                        <li>
                            <Link to="/logout">Logout</Link>
                        </li>
                    </>
                )}
            </ul>
        </nav>
    );
};

export default Navbar;
