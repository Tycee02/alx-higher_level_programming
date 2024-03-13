#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return true;
        this.width = w;
        this.height = h;
    }
};
