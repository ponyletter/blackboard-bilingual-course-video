/**
 * Use the generated sentence_timeline.json data. Do not derive timing from scene narration.
 * `masterTimeline` is the same GSAP timeline used by the video composition.
 */
export function bindSentenceSubtitles(masterTimeline, subtitleElement, sentenceTimeline) {
  subtitleElement.textContent = '';
  subtitleElement.style.opacity = '0';

  for (const item of sentenceTimeline.sentences) {
    // Immediate state changes preserve exact measured start/end boundaries.
    masterTimeline.set(subtitleElement, {
      textContent: item.text,
      opacity: 1,
    }, item.start_seconds);
    masterTimeline.set(subtitleElement, {
      opacity: 0,
      textContent: '',
    }, item.end_seconds);
  }
}

/*
Example integration:

const timelineData = /* inline parsed sentence_timeline.json *\/;
const subtitleElement = document.querySelector('.subtitle');
bindSentenceSubtitles(tl, subtitleElement, timelineData);

Keep .subtitle in the fixed safe zone: bottom: 48px.
Do not fade captions in or out; fading shifts the visual boundary away from the actual sentence WAV interval.
*/
