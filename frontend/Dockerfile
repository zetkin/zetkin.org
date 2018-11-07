FROM node:10
WORKDIR /var/frontend
COPY package.json /var/frontend/package.json
RUN npm install
COPY gulpfile.js /var/frontend/gulpfile.js
CMD ["npm", "run", "watch"]
