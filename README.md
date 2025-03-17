# Electricity Price Tracker and Notification System

This project uses the ComEd API to fetch live hourly electricity prices and sends email notifications when the prices exceed a predefined threshold. Additionally, it integrates with Grafana to visualize electricity price trends and compare them with your EV's charging times to calculate active prices per kWh.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Config](#configuration)
- [Goals](#goals)

## Introduction

The Electricity Price Tracker and Notification System is designed to help you monitor real-time electricity prices and receive alerts when prices are high. By integrating with Grafana, you can also track historical price trends and correlate them with your EV's charging patterns to optimize your energy consumption.

## Features

- **Live Price Fetching**: Fetches hourly electricity prices using the ComEd API.
- **Email Notifications**: Sends email alerts when electricity prices exceed a set threshold.
- **Grafana Integration**: Visualizes electricity price trends and compares them with EV charging times.
- **Active Price Calculation**: Calculates the active price per kWh based on your EV's charging schedule.

## Installation

1. **Clone the Repository**:

## Usage

## Config

## Goals

The primary goal of this project is to provide real-time insights into electricity prices and help optimize energy consumption, especially for EV charging. Here's how the project achieves this:

### 1. Track Electricity Trends
- Use **Grafana** to visualize historical and real-time electricity prices.
- Set up a Grafana dashboard to monitor price fluctuations and identify patterns over time.

### 2. Compare with EV Charging Times
- Correlate electricity prices with your EV's charging schedule to identify the most cost-effective times to charge.
- Import your EV charging data into the system to analyze how charging times align with price trends.

### 3. Calculate Active Prices
- Determine the **active price per kWh** based on your charging patterns and electricity price trends.
- Use the calculated prices to optimize your EV charging schedule and reduce energy costs.

### 4. Automate Notifications
- Set up email notifications to alert you when electricity prices exceed a predefined threshold.
- Stay informed about price spikes and adjust your energy usage accordingly.

### 5. Monitor and Optimize
- Continuously monitor the Grafana dashboard to track electricity trends and compare them with your EV charging schedule.
- Use the insights gained to refine your charging strategy and maximize savings.

By integrating **ComEd API** for live price data, **email notifications** for alerts, and **Grafana** for visualization, this project helps you make data-driven decisions about your energy consumption and EV charging habits.