import React, { useState } from 'react';
import axios from 'axios';

function ProductCreate() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const token = localStorage.getItem('token'); // Pobieramy token z localStorage

    axios.post(
      'http://127.0.0.1:8000/api/products/create/',
      {
        title,
        description,
        price,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`, // Dodajemy nagłówek z tokenem
        },
      }
    )
    .then((response) => {
      console.log(response.data);
      alert('Product created successfully!');
    })
    .catch((error) => {
      console.error('There was an error creating the product!', error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Title:</label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div>
        <label>Description:</label>
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div>
        <label>Price:</label>
        <input
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
      </div>
      <button type="submit">Create</button>
    </form>
  );
}

export default ProductCreate;
