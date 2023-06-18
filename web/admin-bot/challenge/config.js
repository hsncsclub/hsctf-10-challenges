const sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));

const challenges = new Map([
	[
		"fancy-page",
		{
			title: "Submit Page",
			header: "Show us what you've created!",
			timeout: 8 * 1000,
			urlRegex: /^http:\/\/fancy-page\.hsctf\.com\//,
			handler: async function (url, ctx) {
				const URL = "http://fancy-page.hsctf.com/";
				const DOMAIN = "fancy-page.hsctf.com";
				const FLAG = "flag{filter_fail}";
				let page = await ctx.newPage();
				await page.setCookie({
					name: "flag",
					value: FLAG,
					url: URL,
					domain: DOMAIN,
					httpOnly: false,
				});

				await page.goto(url, { timeout: 3000, waitUntil: "domcontentloaded" });
				await sleep(3000);
				await page.close();
			},
		},
	],
	[
		"fancier-page",
		{
			title: "Submit Page",
			header: "Show us what you've created!",
			timeout: 8 * 1000,
			urlRegex: /^http:\/\/fancier-page\.hsctf\.com\//,
			handler: async function (url, ctx) {
				const URL = "http://fancier-page.hsctf.com/";
				const DOMAIN = "fancier-page.hsctf.com";
				const FLAG = "flag{prototype_pollution_kills_thousands_of_websites_each_year}";
				let page = await ctx.newPage();
				await page.setCookie({
					name: "flag",
					value: FLAG,
					url: URL,
					domain: DOMAIN,
					httpOnly: false,
				});

				await page.goto(url, { timeout: 3000, waitUntil: "domcontentloaded" });
				await sleep(3000);
				await page.close();
			},
		},
	],
]);
module.exports = {
	challenges,
};
