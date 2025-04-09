export function load() {
	const scores = Array.from({ length: 22 }, () => Math.floor(Math.random() * 191) + 10);
	return {
		scores,
	};
}