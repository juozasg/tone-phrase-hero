<script>
	import { bestScore } from '$lib/scoreCookie.svelte';
	import { secondsToTime } from '$lib/util';

	// import { goto } from '$app/navigation';
	// goto('/lesson02');

	const lesson01Best = bestScore('lesson01');
	const lesson02Best = bestScore('lesson02');
	const lesson02Unlocked = lesson01Best && lesson01Best <= 120;

	const lesson03Best = bestScore('lesson03');
	const lesson03Unlocked = lesson02Best && lesson02Best <= 120;
</script>

<div class="container main-menu">
	<h1>Chords Hero</h1>
	<h2>Learn to name piano chords</h2>

	<div class="level">
		<button class="btn btn-primary">Level 1: White Keys</button>
		{#if lesson01Best}
			<p>Best Time: {secondsToTime(lesson01Best)}</p>
		{/if}
	</div>

	<div class="level">
		<button class="btn btn-primary" disabled={!lesson02Unlocked}>Level 2: Black Keys</button>
		{#if lesson02Unlocked}
			{#if lesson02Best}
				<p>Best Time: {secondsToTime(lesson02Best)}</p>
			{/if}
		{:else}
			<p>Level 1 under 3 minutes to unlock</p>
		{/if}
	</div>

	<div class="level">
		<button class="btn btn-primary" disabled={!lesson03Unlocked}>Level 3: All Keys</button>
		{#if lesson03Unlocked}
			{#if lesson03Best}
				<p>Best Time: {secondsToTime(lesson03Best)}</p>
			{/if}
		{:else}
			<p>Level 2 under 3 minutes to unlock</p>
		{/if}
	</div>
</div>

<style>
	.btn {
		/* margin: 1rem; */
		/* padding: 1rem 2rem; */
		padding: 10px 10px;
		height: 50px;
		width: 300px;
		font-size: 30px;
		/* border: none; */
		/* border-radius: 0.5rem; */
		/* background-color: #0070f3; */
		/* color: white; */
		/* cursor: pointer; */
		/* transition: background-color 0.3s ease; */
	}

	.level {
		margin-bottom: 2em;
		p {
			margin-top: 0;
			margin-bottom: 0;
			font-size: 20px;
			text-align: left;
			margin-left: 24px;
		}
	}

	.main-menu {
		margin-top: 1rem;
		text-align: center;
		max-width: 720px;
		max-height: 720px;
	}
</style>
