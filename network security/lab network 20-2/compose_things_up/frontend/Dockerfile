# Base image
FROM node:latest

# Create app directory
WORKDIR /app

# Copy package and lock files
COPY package.json yarn.lock ./

# Install app dependencies
RUN yarn install

# Copy app files
COPY . .

# Build the app
RUN yarn build

# Expose the port used by the app
EXPOSE 3000

# Start the app
CMD ["yarn", "start"]
