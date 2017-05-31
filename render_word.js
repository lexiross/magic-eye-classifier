// TODO update path when new version on npm
const MagicEye = require("../MagicEye.js/magiceye.js").MagicEye;
const {Noise} = require("noisejs");
const noise = new Noise(Math.random());

const TUPPERWARE_WORDS = [
  "new phone who dis",
  "wyd ;)",
  "u up?",
  "poop",
  "butt hole",
  "fuck ur feelings",
  "untz untz",
  "q t pie",
  "fart",
  "heyyy",
  "69",
  "drugs",
  "pool party",
  "so high",
  "dick library",
  "fyre fest",
  "all your fault",
  "tyler gary",
  "hannah neil",
  "josh wentworth"
];
const NUM_COLORS = 15;
const WIDTH = 1280;
const HEIGHT = 960;
const NOISE_SCALE = 4 + randHex(16);
const generatePerlinNoise = (x, y) => (1 + noise.perlin2(x / NOISE_SCALE, y / NOISE_SCALE)) / 2;

const words = [];
if (process.argv[2]) {
  words.push(process.argv[2].toUpperCase());
} else {
  for (word of TUPPERWARE_WORDS) {
    words.push(word.toUpperCase());
  }
}

words.forEach((word, i) => {
  const opts = {
    width: WIDTH,
    height: HEIGHT,
    randomFn: generatePerlinNoise
  };

  opts.colors = generatePalette(NUM_COLORS);
  opts.text = word;
  const filename = `image_${i}`;
  opts.output = `../magic-eye-classifier/words/${filename}`;
  MagicEye.render(opts);
});

function randHex(n=256) {
  return Math.floor(Math.random() * n);
}

function randomRGBa() {
	return [randHex(),
					randHex(),
					randHex(),
					255];
}

function generatePalette(numColors) {
	const palette = [];
	for (let i = 0; i < numColors; i++) {
		palette.push(randomRGBa());
	}
	return palette;
}

