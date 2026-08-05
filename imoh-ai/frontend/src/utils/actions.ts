export type Action = {
  tool: string;
  label: string;
};

export function extractActions(text: string): Action[] {
  const regex = /\[\[ACTION:(.*?)\|(.*?)\]\]/g;

  const actions: Action[] = [];
  let match;

  while ((match = regex.exec(text)) !== null) {
    actions.push({
      tool: match[1],
      label: match[2],
    });
  }

  return actions;
}

export function removeActions(text: string): string {
  return text.replace(/\[\[ACTION:.*?\]\]/g, "").trim();
}
