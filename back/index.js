// general + express
const express = require('express');
var bodyParser = require('body-parser')
var cors = require('cors')


// mongo
const connectDB = require('./db/connection');
const mongoose = require("mongoose");

// connect to DB
connectDB();


const app = express();

app.use(express.json())
app.use(express.urlencoded({ extended: true }));
app.use(cors())










//PORT CONNECTION 
const Port = process.env.port || 3000;

app.listen(Port, () => console.log("Server Started"));