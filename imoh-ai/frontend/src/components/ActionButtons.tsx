type Action =
  | {
      tool: string;
      label: string;
    }
  | {
      url: string;
      label: string;
    };

type Props = {
  actions: Action[];
  onSelectTool: (tool: string) => void;
};

export default function ActionButtons({ actions, onSelectTool }: Props) {
  if (actions.length === 0) return null;

  return (
    <div className="action-buttons">
      {actions.map((action, index) => {
        if ("url" in action) {
          return (
            <button
              key={index}
              onClick={() =>
                window.open(action.url, "_blank", "noopener,noreferrer")
              }
            >
              {action.label}
            </button>
          );
        }

        return (
          <button key={action.tool} onClick={() => onSelectTool(action.tool)}>
            {action.label}
          </button>
        );
      })}
    </div>
  );
}
