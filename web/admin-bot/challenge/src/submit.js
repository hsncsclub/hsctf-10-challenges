const path = require("path");
const fs = require("fs");
const mustache = require("mustache");
const server = require("./server");
const config = require("./config");

const submitPage = fs.readFileSync(path.join(__dirname, "submit.html")).toString();

server.run({}, async (req) => {
	const challengeId = req.pathname.slice(1);
	const challenge = config.challenges.get(challengeId);
	if (!challenge) {
		return { statusCode: 404 };
	}
	if (req.method === "GET") {
		const page = mustache.render(submitPage, {
			title: challenge.title,
			header: challenge.header,
			recaptcha_site: process.env.APP_RECAPTCHA_SITE,
			msg: req.query.msg,
			url: req.query.url,
		});
		return {
			statusCode: 200,
			headers: { "content-type": "text/html" },
			body: page,
		};
	}
	if (req.method !== "POST") {
		return { statusCode: 405 };
	}
	const body = new URLSearchParams(req.body);
	const send = (msg) => ({
		statusCode: 302,
		headers: {
			location: `?url=${encodeURIComponent(body.get("url"))}&msg=${encodeURIComponent(msg)}`,
		},
	});

	const url = body.get("url");
	const regex = challenge.urlRegex ?? /^https?:\/\//;
	if (!regex.test(url)) {
		return send(`The URL must match ${regex.source}`);
	}
	const payload = {
		challengeId,
		url,
	};
	console.log("publishing", JSON.stringify(payload));
	await server.publish(payload);
	return send("The admin will visit your URL.");
});
